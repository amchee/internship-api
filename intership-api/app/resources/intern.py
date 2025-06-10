from flask_restful import Resource, reqparse
from app.models.intern import InternModel
from flask_jwt_extended import jwt_required
from flask import request

# Parser to validate incoming JSON data
intern_parser = reqparse.RequestParser()
intern_parser.add_argument('name', type=str, required=True, help="Name of the intern is required")
intern_parser.add_argument('university_id', type=int, required=True, help="University ID is required")
intern_parser.add_argument('description', type=str)  # optional field

class Intern(Resource):
    def get(self, intern_id):
        intern = InternModel.query.get(intern_id)
        if intern:
            return {
                'id': intern.id,
                'name': intern.name,
                'university_id': intern.university_id,
                'description': intern.description
            }, 200
        return {'message': 'Intern not found'}, 404

    def post(self):
        data = intern_parser.parse_args()

        if InternModel.find_by_name(data['name']):
            return {'message': f"Intern with name '{data['name']}' already exists."}, 400

        intern = InternModel(
            name=data['name'],
            university_id=data['university_id'],
            description=data.get('description')
        )
        intern.save_to_db()
        return {'message': 'Intern created successfully.'}, 201

    def delete(self, intern_id):
        intern = InternModel.query.get(intern_id)
        if intern:
            intern.delete_from_db()
            return {'message': 'Intern deleted.'}, 200
        return {'message': 'Intern not found.'}, 404

    def put(self, intern_id):
        data = intern_parser.parse_args()
        intern = InternModel.query.get(intern_id)

        if intern:
            intern.name = data['name']
            intern.university_id = data['university_id']
            intern.description = data.get('description')
        else:
            intern = InternModel(
                name=data['name'],
                university_id=data['university_id'],
                description=data.get('description')
            )

        intern.save_to_db()
        return {'message': 'Intern updated successfully.'}, 200


class InternList(Resource):
    def get(self):
        interns = InternModel.query.all()
        return {'interns': [{
            'id': intern.id,
            'name': intern.name,
            'university_id': intern.university_id,
            'description': intern.description
        } for intern in interns]}, 200

    @jwt_required()
    def post(self):
        data = intern_parser.parse_args()

        if InternModel.find_by_name(data['name']):
            return {'message': f"Intern with name '{data['name']}' already exists."}, 400

        intern = InternModel(
            name=data['name'],
            university_id=data['university_id'],
            description=data.get('description')
        )
        intern.save_to_db()
        return {'message': 'Intern created successfully.'}, 201
