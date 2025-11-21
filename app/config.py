# app/config.py
import pathlib
import connexion
from flask_mongoengine import MongoEngine
from flask_marshmallow import Marshmallow

basedir = pathlib.Path(__file__).resolve().parent.parent

#inicializando connexion
connex_app = connexion.App(__name__, specification_dir=basedir)
app = connex_app.app

#config do MongoDB
app.config["MONGODB_SETTINGS"] = {
        "db": "pessoas_db",
        "host": "mongodb://localhost:27017/pessoas_db"
    }

# inicializando MongoEngine
db = MongoEngine()
db.init_app(app)

mash = Marshmallow(app)