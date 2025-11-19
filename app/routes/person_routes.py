# app/routes/pessoas_routes.py
from flask import Blueprint, jsonify, request, abort
from app.models.person import Person, person_schema, people_schema

person_bp = Blueprint("pessoas", __name__)

# GET /pessoas
@person_bp.get("/")
def list_people():
    person = Person.objects()
    return person_schema.dump(person), 200

# GET /pessoas/<id>
@person_bp.get("/<id>")
def get_person(id):
    person = Person.objects(id=id).first()
    if not person:
        abort(404, description="Pessoa não encontrada")
    return people_schema.dump(person), 200

# POST /pessoas
@person_bp.post("/")
def create_person():
    data = request.get_json()
    sobrenome = data.get("sobrenome")
    if Person.objects(sobrenome=sobrenome):
        abort(406, description=f"Pessoa com sobrenome '{sobrenome}' já existe")
    pessoa = Person(**data).save()
    return people_schema.dump(pessoa), 201

# PUT /pessoas/<id>
@person_bp.put("/<id>")
def update_person(id):
    data = request.json
    person = Person.objects(id=id).first()
    if not person:
        abort(404, description="Pessoa não encontrada")
    person.update(**data)
    person.reload()
    return people_schema.dump(person), 200

# DELETE /pessoas/<id>
@person_bp.delete("/<id>")
def delete_person(id):
    person = Person.objects(id=id).first()
    if not person:
        abort(404, description="Pessoa não encontrada")
    person.delete()
    return jsonify({"mensagem": "Pessoa removida com sucesso"}), 200
