from flask import Flask, jsonify
from .config import config as Config
from flask_cors import CORS


def handle_bad_request(e):
    return jsonify(response=e.description), e.code


def create_app(config_name):
    app = Flask(__name__)
    CORS(app, resources={r'/predict': {'origins': '*'}})
    app.config.from_object(Config[config_name])

    app.register_error_handler(400, handle_bad_request)
    app.register_error_handler(404, handle_bad_request)

    from .controller import falha
    app.register_blueprint(falha.blueprint, url_prefix='/predict')

    return app
