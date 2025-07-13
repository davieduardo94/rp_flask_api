from flask import abort, make_response
from models import Person, people_schema, person_schema

def read_all():
    people = Person.query.all()
    return people_schema.dump(people)

def create(person):
    lname = person.get("lname")
    fname = person.get("fname")

    if lname and lname not in PEOPLE:
        PEOPLE[lname] = {
            "lname" : lname,
            "fname" : fname,
            "timestamp" : get_timestamp()
        }
        return PEOPLE[lname], 201
    else:
        abort(
            406,
            f"Person with last name {lname} already exists",
        )

def read_one(lname):
    if lname in PEOPLE:
        return PEOPLE[lname]
    else:
        abort(
            404, f"Person with last name {lname} not found"
        )

def update(lname, person):
    if lname in PEOPLE:
        PEOPLE[lname]["fname"] = person.get("fname", PEOPLE[lname]["fname"])
        PEOPLE[lname]["timestamp"] = get_timestamp()
        return PEOPLE[lname]
    else:
        abort(
            404,
            f"Person with last name {lname} not found"
        )

def delete(lname):
    if lname in PEOPLE:
        del PEOPLE[lname]
        return make_response(
            f"{lname} successfully deleted", 200
        )
    else:
        abort(
            404,
            f"Person with last name {lname} not found"
        )