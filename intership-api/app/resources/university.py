from flask_restful import Resource, reqparse
from app.models.university import UniversityModel
from app.db import db
from flask_jwt_extended import jwt_required

# Argument parser for university data
university_parser = reqparse.RequestParser()
university_parser.add_argument('name', type=str, required=True, help="University name cannot be blank.")

class University(Resource):
    @classmethod
    def get(cls, university_id):
        university = UniversityModel.query.get(university_id)
        if university:
            return {'id': university.id, 'name': university.name}, 200
        return {'message': 'University not found'}, 404

    @classmethod
    @jwt_required()
    def delete(cls, university_id):
        university = UniversityModel.query.get(university_id)
        if university:
            university.delete_from_db()
            return {'message': 'University deleted.'}, 200
        return {'message': 'University not found.'}, 404

    @classmethod
    @jwt_required()
    def put(cls, university_id):
        data = university_parser.parse_args()
        university = UniversityModel.query.get(university_id)

        if university:
            university.name = data['name']
            university.save_to_db()
            return {'message': 'University updated successfully.'}, 200

        return {'message': 'University not found.'}, 404

class UniversityList(Resource):
    @classmethod
    def get(cls):
        return {'universities': [{'id': uni.id, 'name': uni.name} for uni in UniversityModel.query.all()]}, 200

    @classmethod
    @jwt_required()
    def post(cls):
        data = university_parser.parse_args()
        if UniversityModel.find_by_name(data['name']):
            return {'message': 'University already exists.'}, 400

        university = UniversityModel(name=data['name'])
        university.save_to_db()
        return {'message': 'University created successfully.', 'id': university.id}, 201
