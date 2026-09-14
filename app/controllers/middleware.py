from flask import session, redirect, request

def verificar_sessao():
    if "astronauta" not in session and request.path != "/login":
        return redirect("/login")

def finalizar_requisicao(error):
    print(f"Requisição finalizada. Erro: {error}")
