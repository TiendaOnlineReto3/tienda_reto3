import os
from flask import (
    Flask,
    jsonify,
    request,
    send_from_directory,
    redirect,
    url_for,
    render_template,
)
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from werkzeug.utils import secure_filename
from flask_admin.form.upload import ImageUploadField
from flask_security import (
    Security,
    SQLAlchemyUserDatastore,
    UserMixin,
    RoleMixin,
    login_required,
    current_user,
)
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from flask_login import login_user
from flask import redirect, url_for
from flask_admin import AdminIndexView
from flask_login import current_user, logout_user


app = Flask(__name__)
app.config.from_pyfile("config.py")

# Configura una clave secreta para las sesiones
app.secret_key = "clavesupersecreta12345"  # Reemplaza con una cadena única y secreta

# Configura la carpeta donde se subirán las imágenes
UPLOAD_FOLDER = "img"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Configura la base de datos
db = SQLAlchemy(app)

# Define la tabla roles_users
roles_users = db.Table(
    "roles_users",
    db.Column("user_id", db.Integer(), db.ForeignKey("user.id")),
    db.Column("role_id", db.Integer(), db.ForeignKey("role.id")),
)


# Define el modelo de Role
class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


# Define el modelo de User
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship(
        "Role", secondary=roles_users, backref=db.backref("users", lazy="dynamic")
    )
    fs_uniquifier = db.Column(db.String(255), unique=True)


# Configuración de Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# Configuración de Flask-WTF CSRF
csrf = CSRFProtect(app)


# Define el modelo de Articulo
class Articulo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    imagen = ImageUploadField(
        label="Imagen",
        base_path=app.config["UPLOAD_FOLDER"],
        relative_path="img/",
        url_relative_path="img/",
    )
    descripcion = db.Column(db.String(200))
    categoria = db.Column(db.String(50))


# Crear roles y un usuario administrador por defecto
with app.app_context():
    db.create_all()

    # Buscar un usuario con el email proporcionado
    admin_user = user_datastore.find_user(email="admin@example.com")

    # Crear el usuario administrador si no existe
    if not admin_user:
        admin_user = user_datastore.create_user(
            email="admin@example.com", password="admin"
        )
        user_datastore.create_role(name="admin", description="Administrator")
        user_datastore.add_role_to_user(admin_user, "admin")

    db.session.commit()


# Define la vista personalizada de administrador
class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for("login"))

    def render(self, template, **kwargs):
        # Agregar un enlace/botón de logout en la barra de navegación
        self._template_args["logout_url"] = url_for("logout")
        return super(MyAdminIndexView, self).render(template, **kwargs)


# Crea una instancia de Admin con la vista personalizada
admin = Admin(
    app, name="Admin", index_view=MyAdminIndexView(), template_mode="bootstrap3"
)

# Protege toda la interfaz de administración con el decorador login_required
admin.add_view(
    ModelView(Articulo, db.session, endpoint="admin_articulo", category="Articulos")
)

admin.add_view(ModelView(User, db.session, endpoint="admin_user", category="Usuarios"))

admin.add_view(ModelView(Role, db.session, endpoint="admin_role", category="Roles"))

admin.logout_endpoint = "logout"


# Ruta para servir imágenes estáticas
# @app.route("/img/<filename>")
# def uploaded_file(filename):
#     return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


# Ruta para el login
from forms import LoginForm


# Ruta para el login
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = user_datastore.get_user(form.email.data)
        login_user(user)

        # Imprime información sobre el usuario autenticado
        print(f"Usuario autenticado: {current_user}")

        return redirect(url_for("admin.index_view"))

    return render_template("login.html", form=form)


# Ruta para el logout
@app.route("/logout")
@login_required  # Asegura que solo usuarios autenticados puedan acceder a la ruta de logout
def logout():
    logout_user()
    return redirect(url_for("login"))


# Configura la API
api = Api(app)


# Define la clase para los recursos de Articulo
class ArticuloResource(Resource):
    def get(self, id=None):
        if id:
            articulo = Articulo.query.get(id)
            if articulo:
                return {
                    "id": articulo.id,
                    "nombre": articulo.nombre,
                    "precio": articulo.precio,
                    "imagen": articulo.imagen,
                    "descripcion": articulo.descripcion,
                    "categoria": articulo.categoria,
                }
            else:
                return {"message": "Artículo no encontrado"}, 404
        else:
            articulos = Articulo.query.all()
            return {
                "articulos": [
                    {
                        "id": articulo.id,
                        "nombre": articulo.nombre,
                        "precio": articulo.precio,
                        "imagen": articulo.imagen,
                        "descripcion": articulo.descripcion,
                        "categoria": articulo.categoria,
                    }
                    for articulo in articulos
                ]
            }

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("nombre", type=str, required=True)
        parser.add_argument("precio", type=float, required=True)
        parser.add_argument("imagen", type=str)
        parser.add_argument("descripcion", type=str)
        parser.add_argument("categoria", type=str)

        data = parser.parse_args()

        if "imagen" in request.files and request.files["imagen"]:
            file = request.files["imagen"]
            if file.filename == "":
                return {"message": "No se seleccionó un archivo de imagen"}, 400
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
                file.save(file_path)
                nuevo_articulo = Articulo(
                    nombre=data["nombre"],
                    precio=data["precio"],
                    imagen=file_path,
                    descripcion=data["descripcion"],
                    categoria=data["categoria"],
                )
                db.session.add(nuevo_articulo)
                db.session.commit()
                return {"message": "Artículo creado"}, 201
            else:
                return {"message": "Tipo de archivo no permitido"}, 400

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("nombre", type=str, required=True)
        parser.add_argument("precio", type=float, required=True)
        parser.add_argument("imagen", type=str)
        parser.add_argument("descripcion", type=str)
        parser.add_argument("categoria", type=str)

        data = parser.parse_args()

        articulo = Articulo.query.get(id)
        if articulo:
            articulo.nombre = data["nombre"]
            articulo.precio = data["precio"]
            articulo.imagen = data["imagen"]
            articulo.descripcion = data["descripcion"]
            articulo.categoria = data["categoria"]

            db.session.commit()

            return {"message": "Artículo actualizado"}
        else:
            return {"message": "Artículo no encontrado"}, 404

    def delete(self, id):
        articulo = Articulo.query.get(id)
        if articulo:
            db.session.delete(articulo)
            db.session.commit()
            return {"message": "Artículo eliminado"}
        else:
            return {"message": "Artículo no encontrado"}, 404


# Agrega el recurso Articulo a la API
api.add_resource(ArticuloResource, "/articulo", "/articulo/<int:id>")

if __name__ == "__main__":
    app.run(debug=True, port=4000)
