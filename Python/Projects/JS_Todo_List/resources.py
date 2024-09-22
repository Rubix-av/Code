from flask import jsonify
from flask_restful import Resource, Api, reqparse, fields, marshal_with
from flask_security import auth_required
from models import Todo, User
from extensions import db

parser = reqparse.RequestParser()
parser.add_argument('title', type=str, help="Topic should be string", required=True)
parser.add_argument('desc', type=str, help="Description should be string")
parser.add_argument('date_created', type=str, help="Date should be string")

api = Api(prefix='/api')

todo_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'desc': fields.String,
    'user_id': fields.Integer,
    'date_created': fields.DateTime(dt_format='iso8601')
}

class Todos(Resource):
    @auth_required('token')
    @marshal_with(todo_fields)
    def get(self, id=None):
        if id:
            allTodos = Todo.query.filter_by(user_id=id).all()
            if not allTodos:
                return []
            return allTodos

        else:
            allTodos = Todo.query.all()
            if not allTodos:
                return []
            return allTodos

    @auth_required('token')
    def post(self, id):
        try:
            args = parser.parse_args()        
            todo = Todo(user_id=id, **args)

            db.session.add(todo)
            db.session.commit()
        except:
            db.session.rollback()
            return {"message": "creating todo failed", "todo_id": todo.id}, 420

        return {"message": "todo created", "todo_id": todo.id}, 200

    @auth_required('token')
    def delete(self, id):
        todo = Todo.query.get(id)

        if not todo:
            return {"message": "todo not found"}, 404
        
        try:
            db.session.delete(todo)
            db.session.commit()
            return {"message": "todo deleted successfully"}, 200
        except:
            db.session.rollback()
            return {"message": "error deleting todo"}, 500

class UserProfile(Resource):
    @auth_required('token')
    def get(self, id):
        user = User.query.filter_by(id=id).first()
        if not user:
            return {"message": "user not found"}, 404
        
        user_data = {
            "id": user.id,
            "email": user.email,
            "roles": [role.name for role in user.roles],
        }

        return user_data, 200

api.add_resource(Todos, '/todos/<int:id>', '/todos')
api.add_resource(UserProfile, '/users/<int:id>', '/users')
