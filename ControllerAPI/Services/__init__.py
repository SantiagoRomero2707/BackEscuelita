from .INVIMA import invima
from flask_cors import CORS
from .config import Config
from flask import Flask


def create_app():
    """ Método de configuración de APP. """
    app = Flask(__name__)
    CORS(app)

    # configuración básica
    app.config.from_object(Config)

    # Vistas con  blueprints
    app.register_blueprint(invima)
    return app
