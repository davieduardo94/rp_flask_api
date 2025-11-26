from marshmallow import Schema, fields, ValidationError

# Define a schema with a list of strings
class UserSchema(Schema):
    name = fields.String(required=True)
    tags = fields.List(fields.String(), required=False)

# Example usage
schema = UserSchema()

# Serialize (dump)
user_data = {"name": "Alice", "tags": ["admin", "editor"]}
serialized = schema.dump(user_data)
print("Serialized:", serialized)

# Deserialize (load)
try:
    loaded = schema.load({"name": "Bob", "tags": ["dev", "ops"]})
    print("Deserialized:", loaded)
except ValidationError as err:
    print("Validation errors:", err.messages)
