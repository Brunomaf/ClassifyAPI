from flask import Flask
from .routes.classify import classify_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(classify_bp)
    return app
