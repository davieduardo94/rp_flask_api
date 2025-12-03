# app/routes/pessoas_routes.py
from flask import Blueprint, abort, current_app
from app.models.person import people_schema, person_schema
from datetime import datetime

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

def create_person(body):
    db = current_app.mongo_db
    full_name = body.get("full_name")
    existing_person = db.people.find_one({"full_name" : full_name}, {"_id" : 0})

    if existing_person is None:
        created_date = datetime.now()
        body["created_date"] = created_date
        new_person = person_schema.load(body)
        created_person = db.people.insert_one(new_person)
        return person_schema.dump(created_person)
    else:
        abort(
            406,
            f'Pessoa o nome "{full_name}" já tem cadastro!'
        )

def read_person(full_name):
    db = current_app.mongo_db
    person = db.people.find_one({"full_name" : full_name}, {"_id" : 0})

    if person:
        return person_schema.dump(person)
    else:
        abort(
            404, f"Pessoa com o nome {full_name} não encontrada!"
        )
    
