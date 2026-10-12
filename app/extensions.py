# Importa as extensões utilizadas pelo projeto.
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


# Cria a instância do SQLAlchemy sem associá-la a uma aplicação específica.
db = SQLAlchemy()

# Cria a instância responsável pelas migrações do banco de dados.
migrate = Migrate()

# Cria a instância responsável pelos recursos do Bootstrap.
bootstrap = Bootstrap()

# Cria a instância responsável pela exibição de datas e horários.
moment = Moment()
