import os
from flask import Flask, redirect, url_for, request, send_from_directory, jsonify
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from flask_security import (
    Security,
    SQLAlchemyUserDatastore,
    UserMixin,
    RoleMixin,
    current_user,
)
from flask_wtf.csrf import CSRFProtect
from flask_admin.form.upload import ImageUploadField
from werkzeug.utils import secure_filename
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
)
from werkzeug.local import _request_ctx_stack

app = Flask(__name__)
CORS(app)
app.config.from_pyfile("config.py")

# Configure Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = "login"

# Configure Flask-JWT-Extended
app.config["JWT_SECRET_KEY"] = "your-secret-key"
jwt = JWTManager(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


from flask import render_template


# Define la ruta para el login
@app.route("/login", methods=["POST"])
def login():
    if "email" in request.form and "password" in request.form:
        email = request.form["email"]
        password = request.form["password"]
        user = user_datastore.find_user(email=email)
        if user and security.check_password_hash(user.password, password):
            login_user(user)
            access_token = create_access_token(identity=user.id)
            return jsonify(access_token=access_token), 200
        else:
            return jsonify(message="Invalid email or password"), 401
    else:
        return jsonify(message="Missing email or password"), 400


# Update the logout route
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


# Token-based authentication route
@app.route("/get_token", methods=["POST"])
def get_token():
    if "email" in request.form and "password" in request.form:
        email = request.form["email"]
        password = request.form["password"]
        user = user_datastore.find_user(email=email)
        if user and security.check_password_hash(user.password, password):
            access_token = create_access_token(identity=user.id)
            return {"access_token": access_token}, 200
        else:
            return {"message": "Invalid email or password"}, 401
    else:
        return {"message": "Missing email or password"}, 400


# Define a route for the root URL ("/")
@app.route("/")
def index():
    if current_user.is_authenticated:
        # Si el usuario está logueado, redirige a la página de administrador
        return redirect(url_for("admin.index"))
    else:
        # Si el usuario no está logueado, redirige a la página de login
        return redirect(url_for("security.login"))


@app.route("/images/articulo/<int:id>")
def get_image(id):
    articulo = Articulo.query.get(id)
    if articulo and articulo.imagen:
        return send_from_directory(app.config["UPLOAD_FOLDER"], articulo.imagen)
    else:
        return {"message": "Imagen no encontrada"}, 404


# Configuración de la carpeta donde se subirán las imágenes
UPLOAD_FOLDER = "img"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Configuración de la base de datos
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
csrf.init_app(app)


# Define el modelo de Articulo
class Articulo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    imagen = db.Column(db.String(255))
    descripcion = db.Column(db.String(200))
    categoria = db.Column(db.String(50))


# Crea roles y un usuario administrador por defecto
with app.app_context():
    db.create_all()

    # Busca un usuario con el email proporcionado
    admin_user = user_datastore.find_user(email="admin@example.com")

    # Crea el usuario administrador si no existe
    if not admin_user:
        admin_user = user_datastore.create_user(
            email="admin@example.com", password="admin"
        )
        user_datastore.create_role(name="admin", description="Administrator")
        user_datastore.add_role_to_user(admin_user, "admin")

    db.session.commit()


# Define la vista personalizada de administrador
class MyAdminIndexView(AdminIndexView):
    @expose("/")
    def index(self):
        if not current_user.is_authenticated:
            # If user is not logged in, redirect to the login page
            return redirect(url_for("security.login"))
        return super(MyAdminIndexView, self).index()

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("security.login"))

    def render(self, template, **kwargs):
        self._template_args["logout_url"] = url_for("security.logout")
        return super(MyAdminIndexView, self).render(template, **kwargs)


# Crea una instancia de Admin con la vista personalizada
admin = Admin(
    app, name="Admin", index_view=MyAdminIndexView(), template_mode="bootstrap3"
)


# Define el modelo de vista personalizado
class MyModelView(ModelView):
    form_extra_fields = {
        "imagen": ImageUploadField(
            "Imagen",
            base_path=app.config["UPLOAD_FOLDER"],
            relative_path="img/",
            url_relative_path="img/",
        )
    }

    def create_model(self, form):
        model = self.model()

        image_file = form.imagen.data
        if image_file:
            image_path = os.path.join(
                app.config["UPLOAD_FOLDER"], secure_filename(image_file.filename)
            )
            image_file.save(image_path)
            setattr(model, "imagen", secure_filename(image_file.filename))

        form.populate_obj(model)
        self.session.add(model)
        self._on_model_change(form, model, True)
        self.session.commit()
        return True


# Agrega la vista personalizada al admin
admin.add_view(
    MyModelView(
        Articulo,
        db.session,
        endpoint="admin_articulo_view",
        category="Articulos",
        url="articulo",
    )
)

admin.add_view(ModelView(User, db.session, endpoint="admin_user", category="Usuarios"))
admin.add_view(ModelView(Role, db.session, endpoint="admin_role", category="Roles"))
admin.logout_endpoint = "logout"

# Configuración de la API
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
                    "imagen": url_for("get_image", id=articulo.id),  # Updated line
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
                        "imagen": url_for("get_image", id=articulo.id),  # Updated line
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
            if file and file.filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS:
                image_data = file.read()

                nuevo_articulo = Articulo(
                    nombre=data["nombre"],
                    precio=data["precio"],
                    imagen=image_data,
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

    def get_image(self, id):
        articulo = Articulo.query.get(id)
        if articulo and articulo.imagen:
            return send_from_directory(app.config["UPLOAD_FOLDER"], articulo.imagen)
        else:
            return {"message": "Imagen no encontrada"}, 404


# Agrega el recurso Articulo a la API
api.add_resource(
    ArticuloResource,
    "/articulo",
    "/articulo/<int:id>",
    "/images/<filename>",
    "/images/articulo/<int:id>",
)


if __name__ == "__main__":
    app.run(debug=True, port=4000)
