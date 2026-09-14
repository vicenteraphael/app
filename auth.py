from flask import Blueprint, request, session, redirect, render_template
from data import astronautas

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form.get("usuario", "")
        senha = request.form.get("senha", "")

        if usuario in astronautas and astronautas[usuario]["senha"] == senha:
            session["astronauta"] = usuario
            session["cargo"] = astronautas[usuario]["cargo"]
            return redirect("/painel")

        return "Usuário ou senha inválidos", 401

    return render_template("login.html")

@auth.route("/logout")
def logout():
    session.clear()
    return redirect("/login")
