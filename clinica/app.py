from flask import Flask

from clinica.ext import site
from clinica.ext import config
from clinica.ext import db
from clinica.ext import cli


def create_app(app):
    app = Flask(__name__)

    config.init_app(app)
    db.init_app(app)
    cli.init_app(app)
    site.init_app(app)

    return app
    