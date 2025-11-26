# app/routes/pessoas_routes.py
from flask import Blueprint, abort, current_app
from app.extensions import mongo_client, mongo_db
from app.models.person import people_schema, person_schema

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

def read_person(full_name):
    db = current_app.mongo_db
    person = db.people.find_one({"full_name" : full_name}, {"_id" : 0, "created_date": 0})

    if person:
        return person_schema.dump(person)
    else:
        abort(
            404, f"Pessoa com o nome {full_name} não encontrada!"
        )