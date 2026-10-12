# Importa a função usada para renderizar páginas HTML.
from flask import render_template

# Importa o Blueprint principal da aplicação.
from main import main


# Trata páginas que não foram encontradas.
@main.app_errorhandler(404)
def page_not_found(error):
    # Retorna a página de erro 404 com o código HTTP correspondente.
    return render_template("404.html"), 404


# Trata erros internos do servidor.
@main.app_errorhandler(500)
def internal_server_error(error):
    # Retorna a página de erro 500 com o código HTTP correspondente.
    return render_template("500.html"), 500
