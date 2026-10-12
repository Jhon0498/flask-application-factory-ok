# Importa a classe Blueprint para agrupar as rotas do sistema.
from flask import Blueprint


# Cria o Blueprint principal da aplicação.
main = Blueprint("main", __name__)


# Importa as rotas para registrá-las no Blueprint.
from main import views

# Importa os manipuladores de erros do Blueprint.
from main import errors
