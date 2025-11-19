# app/config.py
import pathlib

basedir = pathlib.Path(__file__).resolve().parent.parent

class Config:
    MONGODB_SETTINGS = {
        "db": "pessoas_db",
        "host": "mongodb://localhost:27017/pessoas_db"
    }

    JSON_SORT_KEYS = False
