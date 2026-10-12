# Importa a função responsável por criar a aplicação.
from app import create_app

# Importa a extensão do banco de dados.
from app.extensions import db

# Importa os modelos para registrar suas tabelas.
from app.models import User, Role, EmailEnviado


# Testa as páginas principais da aplicação.
def test_paginas_principais():
    # Cria a aplicação usando as configurações de teste.
    app = create_app("testing")

    # Abre o contexto necessário para acessar o banco.
    with app.app_context():
        # Cria as tabelas somente no banco de teste em memória.
        db.create_all()

        # Cria o cliente que simula requisições HTTP.
        cliente = app.test_client()

        # Verifica se a página inicial funciona.
        resposta_inicio = cliente.get("/")
        assert resposta_inicio.status_code == 200

        # Verifica se a página de e-mails enviados funciona.
        resposta_emails = cliente.get("/emails-enviados")
        assert resposta_emails.status_code == 200

        # Encerra a sessão do banco de teste.
        db.session.remove()

        # Apaga as tabelas do banco de teste em memória.
        db.drop_all()
