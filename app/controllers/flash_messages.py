from flask import request, flash, redirect, Blueprint, render_template

flash_messages = Blueprint("flash_messages", __name__)

@flash_messages.route("/missao/nova", methods=["GET", "POST"])
def nova_missao():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()

        if not nome:
            flash("Nome da missão não pode ser vazio.", "alerta")
            return redirect("/missao/nova")

        from app.models.dados import proximo_id

        nova = {
            "id": proximo_id,
            "nome": nome,
            "destino": request.form.get("destino", ""),
            "status": "Preparando",
            "classificada": False,
        }

        import app.models.dados as dados

        dados.missoes.append(nova)
        dados.proximo_id += 1

        flash("Missão cadastrada com sucesso!", "sucesso")
        return redirect("/painel")
    
    return render_template('cadastro_missao.html')