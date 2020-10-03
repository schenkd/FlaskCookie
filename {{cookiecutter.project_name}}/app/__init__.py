from flask import Flask
from app.config import config


def create_app(config_name: str):
    """
    Factory to create Flask application context based on choosen config.

    Args:
        config_name: Configname

    Returns:
        Flask application context
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from app.api import api
    app.register_blueprint(api, url_prefix='/api')

    return app
