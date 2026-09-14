from flask import Flask

from app import *

app = Flask(__name__, template_folder='app/templates')
app.secret_key = "chave-secreta"

# Middleware
app.before_request(verificar_sessao)
app.teardown_request(finalizar_requisicao)

# Blueprints
app.register_blueprint(auth)
app.register_blueprint(cookies)
app.register_blueprint(erros)
app.register_blueprint(flash_messages)
app.register_blueprint(logs)

if __name__ == "__main__":
    app.run(debug=True)
