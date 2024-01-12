from flask import Flask
from .route import log

def create_app():
    app = Flask(__name__)

    app.register_blueprint(log.bp)

    return app