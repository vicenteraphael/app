from flask import session, abort, Blueprint

from app.models.dados import missoes

erros = Blueprint("erros", __name__)

@erros.route("/missao/<int:id>")
def ver_missao(id):
    for missao in missoes:
        if missao["id"] == id:
            if missao["classificada"] and session.get("cargo") != "Comandante":
                abort(401)

            return missao

    abort(404)

@erros.errorhandler(404)
def erro_404(error):
    return {"erro": "Rota espacial não localizada"}, 404