from flask import Flask
import os
import ssl
from flask_cors import CORS
from .api import api as api_blueprint


class Config:
    UPLOAD_FOLDER = os.path.join(os.getcwd(), "app/dumps")


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    app.register_blueprint(api_blueprint)

    return app
