# app/extensions.py
from flask_marshmallow import Marshmallow
from pymongo import MongoClient
from .config import Config

URI = Config.MONGO_URI
DB_NAME = Config.DB_NAME
mongo_client = MongoClient(URI)
mongo_db = mongo_client[DB_NAME]

mash = Marshmallow()
