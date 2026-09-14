# Revisão - Laboratório de Programação 1

Resolução modularizada da atividade de revisão sobre o Painel de Controle Espacial.

## Estrutura

- `app.py` — criação da aplicação, configuração e registro dos Blueprints/middleware.
- `data.py` — dados fornecidos no enunciado.
- `middleware.py` — `before_request` e `teardown_request`.
- `auth.py` — Blueprint de autenticação, login e logout.
- `routes.py` — cookies, painel, flash messages, missões, erros e alteração de status.
- `logging_config.py` — configuração do logging básico em `missoes.log`.
- `templates/` — páginas Jinja2.
- `requirements.txt` — dependência Flask.

## Como executar

1. Instale as dependências:
   `pip install -r requirements.txt`

2. Inicie:
   `python app.py`

3. Acesse:
   `http://127.0.0.1:5000/login`

## Usuários do enunciado

- `neil` / `apollo11` — Comandante
- `buzz` / `lunar99` — Piloto

## Observação

O `logging_config.py` deve ser importado antes das operações que precisam ser registradas. Para isso, execute a aplicação com:

`python -c "import logging_config; import app"`

ou, de forma mais simples, importe `logging_config` no início de `app.py`.

