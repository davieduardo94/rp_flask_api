# app/models/pessoa.py
from app.extensions import db, mash
from datetime import datetime

class Person(db.Document):
    full_name = db.StringField(required=True, max_length=32)
    age = db.IntField(required=True, min_value=0, max_value=150)
    phone_number = db.ListField(db.StringField())
    created_date = db.DateTimeField(default=datetime.now)

class PersonSchema(mash.Schema):
    class Meta:
        fields = ("id", "full_name", "age", "created_date")

people_schema = PersonSchema() # 1 pessoa
person_schema = PersonSchema(many=True) # varias pessoas