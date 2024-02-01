from Admin import create_app, db
from flask import render_template, jsonify
from flask_login import current_user, login_required
from Admin.models import Articulo  # Asegúrate de importar tu modelo Articulo

app = create_app()


@app.route("/articulos")
@login_required
def articulos():
    return render_template("articulos.html", user=current_user)


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


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
