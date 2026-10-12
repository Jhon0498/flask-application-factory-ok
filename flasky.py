# Importa a função responsável por criar a aplicação Flask.
from app import create_app

# Cria a aplicação usando as configurações do ambiente.
app = create_app()

# Executa o servidor local quando este arquivo é iniciado diretamente.
if __name__ == "__main__":
    # Inicia o servidor em modo de depuração para desenvolvimento local.
    app.run(debug=app.config.get("DEBUG", False))
