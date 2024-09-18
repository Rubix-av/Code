from flask import jsonify
from flask_restful import Resource, Api, reqparse, fields, marshal_with
from flask_security import auth_required
from models import Todo
from extensions import db

parser = reqparse.RequestParser()
parser.add_argument('title', type=str, help="Topic should be string", required=True)
parser.add_argument('desc', type=str, help="Description should be string")

api = Api(prefix='/api')

todo_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'desc': fields.String,
    'user_id': fields.Integer
}

class Todos(Resource):
    @auth_required('token')
    @marshal_with(todo_fields)
    def get(self):
        allTodos = Todo.query.all()

        if not allTodos:
            return jsonify({"message": "No todos found"}), 404  # Return a 404 or appropriate status code

        return allTodos

    @auth_required('token')
    def post(self):
        args = parser.parse_args()
        todo = Todo(user_id=1, **args)
        db.session.add(todo)
        db.session.commit()
        return jsonify({"message": "todo created"})

api.add_resource(Todos, '/todos')
