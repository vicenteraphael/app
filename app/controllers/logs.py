import logging
from flask import request,  Blueprint

from app.models.dados import missoes

logs = Blueprint("logs", __name__)

logging.basicConfig(
    filename="app/logs/missoes.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

@logs.route("/missao/<int:id>/status", methods=["PUT"])
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