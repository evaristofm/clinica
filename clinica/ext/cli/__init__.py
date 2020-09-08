import click
from clinica.ext.db import db
from clinica.ext.db import models #noqa



def init_app(app):

    @app.cli.command()
    def create_db():
        """Inicializa um banco de dados """
        db.create_all()

    @app.cli.command()
    def listar_users():
        return click.echo("Lista de usuários")