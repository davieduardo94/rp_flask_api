# app/routes/pessoas_routes.py
from flask import Blueprint, current_app
from app.extensions import mongo_client, mongo_db
from app.models.person import people_schema

people_bp = Blueprint("people", __name__)

# GET /pessoas
@people_bp.get("/")
def list_people():
    db = current_app.mongo_db
    docs = db.people.find() # buscar todos os documentos da coleção
    people_list = []

    for doc in docs:
        # convertendo ObjectId para str (json)
        doc["id"] = str(doc["_id"])
        del doc["_id"]
        people_list.append(doc)

    return people_schema.dump(people_list)

