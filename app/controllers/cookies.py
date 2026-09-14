from flask import make_response, redirect, request, session, Blueprint

from app.models.dados import missoes

cookies = Blueprint("cookies", __name__)

@cookies.route("/idioma/<escolha>")
def idioma(escolha):
    resposta = make_response(redirect("/painel"))
    resposta.set_cookie("idioma", escolha, max_age=7 * 24 * 60 * 60)
    return resposta

@cookies.route("/painel")
def painel():
    idioma_atual = request.cookies.get("idioma", "pt")
    return {
        "mensagem": "Painel de Controle Espacial",
        "astronauta": session.get("astronauta"),
        "cargo": session.get("cargo"),
        "idioma": idioma_atual,
        "missoes": missoes,
    }