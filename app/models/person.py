# app/models/pessoa.py
from app.config import mash
from marshmallow import Schema, fields

class PersonSchema(Schema):
    _id = fields.Str()   # _id convertido STR
    full_name = fields.Str(required=True)
    age = fields.Int(required=True)
    phone_number = fields.List(fields.Str())
    created_date = fields.DateTime()


people_schema = PersonSchema() # 1 pessoa
person_schema = PersonSchema(many=True) # varias pessoas