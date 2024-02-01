from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Articulo
from . import db
import json

views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template("home.html", user=current_user)


@views.route("/crear", methods=["GET", "POST"])
@login_required
def crear():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        descripcion = request.form.get("descripcion")
        precio = request.form.get("precio")
        imagen = request.form.get("imagen")
        categoria = request.form.get("categoria")

        if not nombre or not precio:
            flash("Nombre y Precio son obligatorios", category="error")
        else:
            nuevo_articulo = Articulo(
                nombre=nombre,
                descripcion=descripcion,
                precio=precio,
                imagen=imagen,
                categoria=categoria,
                user_id=current_user.id,
            )
            db.session.add(nuevo_articulo)
            db.session.commit()
            flash("Artículo creado correctamente", category="success")
            return redirect(
                url_for("views.crear")
            )  # Redirige después de crear el artículo

    return render_template("crear.html", user=current_user)


@views.route("/delete-articulo/<int:articulo_id>", methods=["POST"])
def delete_articulo(articulo_id):
    articulo = Articulo.query.get(articulo_id)
    if articulo:
        if articulo.user_id == current_user.id:
            db.session.delete(articulo)
            db.session.commit()
            flash("Articulo eliminado!", category="success")
        else:
            flash("No tienes permisos para eliminar este Articulo", category="error")

    return redirect(url_for("views.crear"))
