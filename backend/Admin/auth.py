from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            flash("Login satisfactorio!", category="success")
            login_user(user, remember=True)
            return redirect(url_for("views.home"))
        else:
            flash("Credenciales incorrectas, intentalo de nuevo.", category="error")

    return render_template("login.html", user=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))


@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        first_name = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        user = User.query.filter_by(email=email).first()
        if user:
            flash("El Email ya existe.", category="error")
        elif len(email) < 4:
            flash("Email debe tener más de tres caracteres.", category="error")
        elif len(first_name) < 2:
            flash("El nombre debe tener más de 1 caracter.", category="error")
        elif password1 != password2:
            flash("Las contraseñas no coinciden.", category="error")
        elif len(password1) < 5:
            flash("La contraseña debe tener al menos 5 caracteres.", category="error")
        else:
            new_user = User(
                email=email,
                first_name=first_name,
                password=generate_password_hash(password1, method="pbkdf2:sha256"),
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("Cuenta creada exitosamente!", category="success")
            return redirect(url_for("views.home"))

    return render_template("sign_up.html", user=current_user)
