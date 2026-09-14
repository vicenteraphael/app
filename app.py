import logging_config

from flask import Flask
from middleware import verificar_sessao, finalizar_requisicao
from auth import auth
from routes import main

app = Flask(__name__)
app.secret_key = "chave-secreta"

# Middleware
app.before_request(verificar_sessao)
app.teardown_request(finalizar_requisicao)

# Blueprints
app.register_blueprint(auth)
app.register_blueprint(main)

if __name__ == "__main__":
    app.run(debug=True)
