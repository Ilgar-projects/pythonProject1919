from setup_db import db
from marshmallow import Schema, fields


class User(db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String)
	password = db.Column(db.String)
	role = db.Column(db.String)

class UserSchema(Schema):
	username = fields.Str(required=True)
	password = fields.Str(required=True)
	role = fields.Str(required=True)
