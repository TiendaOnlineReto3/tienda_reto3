from flask_restful import Api, Resource
from Admin import create_app, db
from flask import render_template, jsonify, request, redirect, url_for, send_file
from flask_login import current_user, login_required
from Admin.models import Articulo
import os
from werkzeug.utils import secure_filename
import base64
import io

app = create_app()
api = Api(app)


# MAX_FILE_SIZE = 250 * 1024  # 250KB


def save_uploaded_file(file):
    try:
        file_data = file.read()
        return base64.b64encode(file_data)
    except Exception as e:
        raise ValueError(f"No se pudo leer el archivo: {str(e)}")


@app.route("/articulos")
@login_required
def articulos():
    return render_template("articulos.html", user=current_user)


# Ruta para obtener la imagen del articulo
@app.route("/api/articulos/imagen/<int:articulo_id>")
def obtener_imagen_articulo(articulo_id):
    articulo = Articulo.query.get(articulo_id)

    if articulo is None or articulo.imagen is None:
        return "Artículo no encontrado", 404

    # Decodifica los datos binarios
    imagen_decodificada = base64.b64decode(articulo.imagen)

    # Devuelve la imagen como respuesta con el tipo de contenido adecuado
    return send_file(io.BytesIO(imagen_decodificada), mimetype="image/jpeg")


# Agrega la ruta para eliminar artículos
@app.route("/delete-articulo/<int:articulo_id>", methods=["DELETE"])
@login_required
def delete_articulo(articulo_id):
    # Busca el artículo por su ID
    articulo = Articulo.query.get(articulo_id)

    # Si el artículo no existe, retorna un error
    if not articulo:
        return jsonify({"error": "Artículo no encontrado"}), 404

    # Verifica que el usuario actual sea el propietario del artículo (puedes ajustar esto según tu lógica)
    if articulo.user_id != current_user.id:
        return jsonify({"error": "No tienes permisos para eliminar este artículo"}), 403

    # Elimina el artículo de la base de datos
    db.session.delete(articulo)
    db.session.commit()

    # Retorna una respuesta JSON indicando el éxito
    return jsonify({"success": True})


# API
# Creacion de la ruta de la API
class ArticuloResource(Resource):
    @login_required
    def get(self, articulo_id):
        articulo = Articulo.query.get(articulo_id)
        if articulo:
            return jsonify(
                {
                    "id": articulo.id,
                    "nombre": articulo.nombre,
                    "descripcion": articulo.descripcion,
                    "precio": articulo.precio,
                    "imagen": articulo.imagen,
                }
            )
        else:
            return jsonify({"error": "Artículo no encontrado"}), 404


class ArticulosResource(Resource):
    @login_required
    def get(self):
        articulos = Articulo.query.filter_by(user_id=current_user.id).all()
        return jsonify(
            [
                {
                    "id": articulo.id,
                    "nombre": articulo.nombre,
                    "descripcion": articulo.descripcion,
                    "precio": articulo.precio,
                    "imagen": articulo.imagen,
                }
                for articulo in articulos
            ]
        )

    @login_required
    def post(self):
        try:
            data = request.form
            imagen_file = request.files.get("imagen")

            if not imagen_file:
                return jsonify({"error": "Imagen no proporcionada"}), 400

            nuevo_articulo = Articulo(
                nombre=data.get("nombre"),
                descripcion=data.get("descripcion"),
                precio=data.get("precio"),
                imagen=save_uploaded_file(imagen_file),
                categoria=data.get("categoria"),
                user_id=current_user.id,
            )

            db.session.add(nuevo_articulo)
            db.session.commit()

            # Realiza la redirección después de la creación exitosa
            return redirect(url_for("views.crear"))

        except ValueError as e:
            return jsonify({"error": str(e)}), 400


api.add_resource(ArticuloResource, "/api/articulo/<int:articulo_id>")
api.add_resource(ArticulosResource, "/api/articulos")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
