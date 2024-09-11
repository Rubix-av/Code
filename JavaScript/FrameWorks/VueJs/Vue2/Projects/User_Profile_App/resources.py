from flask_restful import Resource, Api, fields, marshal_with, reqparse
from flask_security.decorators import auth_required, roles_required
from extensions import db
from models import StudyResource

api = Api(prefix='/api')

parser = reqparse.RequestParser() # convert json data to dictionary

parser.add_argument('id', type=int)
parser.add_argument('topic', type=str)
parser.add_argument('content', type=str)
parser.add_argument('creator_id', type=int)

study_materials_fields = {
    'id': fields.Integer,
    'topic': fields.String,
    'content': fields.String,
    'creator': fields.Integer
}

class StudyMaterials(Resource):
    @auth_required()
    @marshal_with(study_materials_fields)

    def get(self):
        all_resources = StudyResource.query.all()
        return all_resources
    
    def post(self):
        args = parser.parse_args()
        study_resource = StudyResource(id=args.id, topic=args.topic, content=args.content, creator_id=args.creator_id)
        db.session.add(study_resource)
        db.session.commit()
        return {"message": "resource created"}, 200

api.add_resource(StudyMaterials, '/resources')


