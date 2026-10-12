# Importa o módulo para acessar as variáveis de ambiente.
import os
from dotenv import load_dotenv

# Carrega as variáveis definidas no arquivo .env.
load_dotenv()


# Define as configurações básicas da aplicação.
class Config:
    # Define a chave secreta usada pelo Flask.
    SECRET_KEY = os.environ.get("SECRET_KEY") or os.environ.get("FLASK_SECRET_KEY", "chave-local-desenvolvimento")

    # Define o endereço do banco de dados.
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:////home/Jhonatan1701/usuarios.db"
    )

    # Desativa o rastreamento de modificações dos objetos do banco.
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Define o administrador que receberá as notificações.
    FLASKY_ADMIN = os.environ.get("FLASKY_ADMIN", "")

    # Define a chave da API do Mailgun.
    MAILGUN_API_KEY = os.environ.get("MAILGUN_API_KEY", "")

    # Define o domínio usado para enviar e-mails.
    MAILGUN_DOMAIN = os.environ.get("MAILGUN_DOMAIN", "")

    # Define o endereço da API do Mailgun.
    MAILGUN_BASE_URL = os.environ.get(
        "MAILGUN_BASE_URL",
        "https://api.mailgun.net"
    )


# Define as configurações para desenvolvimento.
class DevelopmentConfig(Config):
    # Ativa o modo de depuração durante o desenvolvimento.
    DEBUG = True


# Define as configurações para testes.
class TestingConfig(Config):
    # Ativa o modo de testes.
    TESTING = True

    # Usa um banco separado em memória para os testes.
    SQLALCHEMY_DATABASE_URI = "sqlite://"


# Define as configurações para produção.
class ProductionConfig(Config):
    # Desativa o modo de depuração em produção.
    DEBUG = False


# Relaciona os nomes dos ambientes às respectivas configurações.
config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": ProductionConfig,
}
