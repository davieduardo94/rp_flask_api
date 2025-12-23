# app/models/pessoa.py
from marshmallow import Schema, fields

class PersonSchema(Schema):
    _id = fields.Str()   # _id convertido STR
    full_name = fields.Str(required=True)
    age = fields.Int()
    phone_number = fields.List(fields.Str())
    created_date = fields.DateTime()


person_schema = PersonSchema() # 1 pessoa
people_schema = PersonSchema(many=True) # varias pessoas