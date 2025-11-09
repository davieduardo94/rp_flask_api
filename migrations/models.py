# models.py

from datetime import datetime
from marshmallow_sqlalchemy import fields
from config import db, mash

class Note(db.Model):
    __tablename__ = "note"
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey("person.id"))
    content = db.Column(db.String, nullable=False)
    timestamp = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now
    )


class NoteSchema(mash.SQLAlchemyAutoSchema):
    class Meta:
        model = Note
        load_instance = True
        sqla_session = db.session
        include_fk = True


class Person(db.Model):
    __tablename__ = "person"
    id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32), unique=True)
    fname = db.Column(db.String(32))
    timestamp = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now
    )
    notes = db.relationship( #criando o relacionamento com a tabela NOTES
        Note,
        backref = "person",
        cascade = "all, delete, delete-orphan",
        single_parent = True,
        order_by = "desc(Note.timestamp)" 
    )

# mashmallow convert os dados para JSON
class PersonSchema(mash.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        load_instance = True
        sqla_session = db.session
        include_relationships = True
        
    notes = fields.Nested(NoteSchema, many=True)


note_schema = NoteSchema()
person_schema = PersonSchema()
people_schema = PersonSchema(many=True)