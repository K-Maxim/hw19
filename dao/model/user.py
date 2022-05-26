from setup_db import db
from marshmallow import Schema, fields
from sqlalchemy import Column, String, Integer


class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    role = Column(String)


class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    password = fields.Str()
    role = fields.Str()

