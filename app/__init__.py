from flask import Flask
from .config import Config
from .extensions import db
from .routes.pessoas_routes import pessoas_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    app.register_blueprint(pessoas_bp, url_prefix="/pessoas")
    return app
