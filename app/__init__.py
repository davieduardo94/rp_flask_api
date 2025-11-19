# app/__init__.py
import pathlib
import connexion
from pathlib import Path
from flask import render_template
from app.config import Config
from app.extensions import db, mash
from routes.person_routes import person_bp

basedir = pathlib.Path(__file__).parent.resolve()

# Cria app Connexion e adiciona o Swagger file
connex_app = connexion.App(__name__, specification_dir=str(basedir))
connex_app.add_api("swagger.yaml")

# Flask interno
app = connex_app.app
app.config.from_object(Config)

# Inicializa extensões
db.init_app(app)
mash.init_app(app)

# Registra blueprint
app.register_blueprint(person_bp, url_prefix="/pessoas")

# Página inicial (home.html)
@app.route("/")
def home():
    pessoas = db.connection["pessoas_db"]["pessoa"].find()
    return render_template("home.html", people=pessoas)
