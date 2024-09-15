from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    name = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    hobby = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(150), nullable=False)
