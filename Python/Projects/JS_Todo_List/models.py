from extensions import db
from flask_security.core import UserMixin, RoleMixin
from flask_security.models import fsqla_v3 as fsqla
from sqlalchemy.sql import func

fsqla.FsModels.set_db_info(db)

class UserRoles(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String, nullable = False, unique = True)
    password = db.Column(db.String)
    active = db.Column(db.Boolean)
    fs_uniquifier = db.Column(db.String(65), unique = True, nullable = False)
    roles = db.relationship('Role', secondary='user_roles')
    todos = db.relationship('Todo', backref='user')

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), unique = True)
    description = db.Column(db.String(255))

class Todo(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
