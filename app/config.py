# app/config.py ---> CONEXÃO E INICIALIZAÇÃO DO BANCO

# import pathlib
# import connexion
# import os
# from pymongo import MongoClient
# from flask_marshmallow import Marshmallow
# from dotenv import load_dotenv

# # carregar arquivo .env
# load_dotenv()

# basedir = pathlib.Path(__file__).resolve().parent.parent

# #inicializando connexion
# connex_app = connexion.App(__name__, specification_dir=basedir)
# app = connex_app.app

# # pegar variáveis do .env
# MONGO_USER = os.getenv("MONGO_USER")
# MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
# CLUSTER_NAME = os.getenv("CLUSTER_NAME")
# DB_NAME = os.getenv("DB_NAME")
# APP_NAME = os.getenv("APP_NAME")

# MONGO_URI = (
#     f"mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@{CLUSTER_NAME}.ryunxve.mongodb.net/?appName={APP_NAME}"
# )

# #config do MongoDB
# app.config["MONGO_URI"] = MONGO_URI

# # inicializando PyMongo
# client = MongoClient(MONGO_URI)

# # Referência ao banco: pessoas_db
# db = client[DB_NAME]

# # Inicializar Marshmallow
# mash = Marshmallow(app)


import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGO_USER = os.getenv("MONGO_USER")
    MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
    CLUSTER_NAME = os.getenv("CLUSTER_NAME")
    DB_NAME = os.getenv("DB_NAME")
    APP_NAME = os.getenv("APP_NAME")

    MONGO_URI = (
        f"mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@{CLUSTER_NAME}.ryunxve.mongodb.net/{DB_NAME}"
    )
