# app/__init__.py

import pathlib
import connexion
from flask import render_template
from pymongo import MongoClient
from .config import Config
from .extensions import mash, mongo_client, mongo_db   # marshmallow inicializado aqui
from .routes.people_routes import people_bp

# Caminho base
basedir = pathlib.Path(__file__).parent.resolve()

# 1) Criar o Connexion App
connex_app = connexion.App(__name__, specification_dir=str(basedir))
connex_app.add_api("swagger.yaml")  # importa o swagger

# Flask "interno" do Connexion
app = connex_app.app

# Carregar configurações do config.py
app.config.from_object(Config)

# Disponibilizar para o projeto inteiro
app.mongo_client = mongo_client
app.mongo_db = mongo_db

# 2) Inicializar Marshmallow
mash.init_app(app)

# 3) Registrar Blueprints
app.register_blueprint(people_bp, url_prefix="/people")

# 4) Rota inicial (opcional)
@app.route("/")
def home():
    peopple = list(mongo_db.people.find())  # nome da coleção
    return render_template("home.html", people=peopple)
