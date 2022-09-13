# imports
from flask import Flask
from .view import pages


def create_app():
    """ Método de configuración de APP. """
    app = Flask(__name__, template_folder="templates/pages", static_folder="templates/static")
    app.register_blueprint(pages)
    app.run(debug=True, port=5000)
    # Vistas con  blueprints
    return app
