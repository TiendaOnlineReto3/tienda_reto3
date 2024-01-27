# importaciones
from flask import Flask
from flask import jsonify
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy

# aplicación init
app = Flask(__name__)
app.config.from_pyfile("config.py")

# inicialización de la base de datos
db = SQLAlchemy(app)


# definición del modelo de datos
# Esto crea una tabla en la base de datos con los campos que se definen aquí
class Articulo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    imagen = db.Column(db.String(200))
    descripcion = db.Column(db.String(200))
    categoria = db.Column(db.String(50))


# Esto es para crear la tabla en la base de datos
with app.app_context():
    # creación de la tabla
    db.create_all()


# Rutas
# Las rutas son los endpoints que se pueden acceder desde el navegador
@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Tienda Online"})


api = Api(app)


# CRUD
# recurso para la manipulación de artículos
class ArticuloResource(Resource):
    # esto es para obtener un artículo (GET)
    def get(self, id=None):
        if id:
            # Obtener un artículo por ID
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
            # Obtener todos los artículos
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

    # esto es para crear un nuevo artículo (POST)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("nombre", type=str, required=True)
        parser.add_argument("precio", type=float, required=True)
        parser.add_argument("imagen", type=str)
        parser.add_argument("descripcion", type=str)
        parser.add_argument("categoria", type=str)

        data = parser.parse_args()

        nuevo_articulo = Articulo(
            nombre=data["nombre"],
            precio=data["precio"],
            imagen=data["imagen"],
            descripcion=data["descripcion"],
            categoria=data["categoria"],
        )

        db.session.add(nuevo_articulo)
        db.session.commit()

        return {"message": "Artículo creado"}, 201

    # esto es para actualizar un artículo (PUT)
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

    # esto es para eliminar un artículo (DELETE)
    def delete(self, id):
        articulo = Articulo.query.get(id)
        if articulo:
            db.session.delete(articulo)
            db.session.commit()
            return {"message": "Artículo eliminado"}
        else:
            return {"message": "Artículo no encontrado"}, 404


# Esto es para poder obtener los artículos desde la base de datos y verlos en el navegador
api.add_resource(ArticuloResource, "/articulo", "/articulo/<int:id>")
# Final CRUD

# app.run es para que la aplicación se ejecute en el puerto 4000
if __name__ == "__main__":
    app.run(debug=True, port=4000)
