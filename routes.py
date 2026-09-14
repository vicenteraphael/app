import logging

from flask import (
    Blueprint,
    request,
    redirect,
    make_response,
    flash,
    session,
    abort,
)

from data import missoes

main = Blueprint("main", __name__)

@main.route("/idioma/<escolha>")
def idioma(escolha):
    resposta = make_response(redirect("/painel"))
    resposta.set_cookie("idioma", escolha, max_age=7 * 24 * 60 * 60)
    return resposta

@main.route("/painel")
def painel():
    idioma_atual = request.cookies.get("idioma", "pt")
    return {
        "mensagem": "Painel de Controle Espacial",
        "astronauta": session.get("astronauta"),
        "cargo": session.get("cargo"),
        "idioma": idioma_atual,
        "missoes": missoes,
    }

@main.route("/missao/nova", methods=["POST"])
def nova_missao():
    nome = request.form.get("nome", "").strip()

    if not nome:
        flash("Nome da missão não pode ser vazio.", "alerta")
        return redirect("/painel")

    from data import proximo_id

    nova = {
        "id": proximo_id,
        "nome": nome,
        "destino": request.form.get("destino", ""),
        "status": "Preparando",
        "classificada": False,
    }

    missoes.append(nova)

    # Atualiza o contador no módulo de dados.
    import data
    data.proximo_id += 1

    flash("Missão cadastrada com sucesso!", "sucesso")
    return redirect("/painel")

@main.route("/missao/<int:id>")
def ver_missao(id):
    for missao in missoes:
        if missao["id"] == id:
            if missao["classificada"] and session.get("cargo") != "Comandante":
                abort(401)

            return missao

    abort(404)

@main.errorhandler(404)
def erro_404(error):
    return {"erro": "Rota espacial não localizada"}, 404

@main.route("/missao/<int:id>/status", methods=["PUT"])
def alterar_status(id):
    dados = request.get_json(silent=True) or {}
    novo_status = dados.get("novo_status")

    if not novo_status:
        logging.warning("Tentativa de alterar status com valor vazio.")
        return {"erro": "Status não informado"}, 400

    for missao in missoes:
        if missao["id"] == id:
            missao["status"] = novo_status
            logging.info(
                f"Status da missão {id} alterado para {novo_status}."
            )
            return missao

    logging.error(f"Missão {id} não encontrada.")
    return {"erro": "Missão não encontrada"}, 404