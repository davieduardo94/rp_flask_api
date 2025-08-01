from flask import abort, make_response
from config import db
from models import Person, people_schema, person_schema, PersonSchema

def read_all():
    people = Person.query.all()
    person_schema = PersonSchema(many=True)
    return person_schema.dump(people)

def create(body):
    lname = body.get("lname")
    existing_person = Person.query.filter(Person.lname == lname).one_or_none() #verificando se já existe

    if existing_person is None:
        new_person = person_schema.load(body, session=db.session)
        db.session.add(new_person) #adicionando ao banco
        db.session.commit()
        return person_schema.dump(new_person),201
    else:
        abort(
            406,
            f"Person with last name {lname} already exists",
        )

def read_one(lname):
    person = Person.query.filter(Person.lname == lname).one_or_none()
    if person is not None:
        return person_schema.dump(person)
    else:
        abort(
            404, f"Person with last name {lname} not found"
        )

def update(lname, person):
    existing_person = Person.query.filter(Person.lname == lname).one_or_none()
    if existing_person:
        update_person = person_schema.load(person, session=db.session)
        existing_person.fname = update_person.fname
        db.session.merge(existing_person)
        db.session.commit()
        return person_schema.dump(existing_person),201
    else:
        abort(
            404,
            f"Person with last name {lname} not found"
        )

def delete(lname):
    existing_person = Person.query.filter(Person.lname == lname).one_or_none()

    if existing_person:
        db.session.delete(existing_person)
        db.session.commit()
        return make_response("f{lname} succesfully deleted"), 200
    else:
        abort(
            404,
            f"Person with last name {lname} not found"
        )