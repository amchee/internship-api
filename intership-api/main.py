from flask import Flask
from flask_restful import Api
from app.db import db
from app.resources.user import UserRegister, UserLogin
from app.resources.intern import Intern, InternList
from app.resources.university import University, UniversityList
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # JWT Configurations (Required!)
    app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this in production
    app.config['JWT_TOKEN_LOCATION'] = ['headers']
    app.config['JWT_HEADER_NAME'] = 'Authorization'
    app.config['JWT_HEADER_TYPE'] = 'Bearer'

    db.init_app(app)
    jwt = JWTManager(app)
    api = Api(app)

    with app.app_context():
        db.create_all()

    # User endpoints
    api.add_resource(UserRegister, '/register')
    api.add_resource(UserLogin, '/login')

    # Intern endpoints
    api.add_resource(InternList, '/interns')  # POST & GET
    api.add_resource(Intern, '/interns/<int:intern_id>')  # GET, PUT, DELETE

    # University endpoints
    api.add_resource(UniversityList, '/universities')  # POST & GET
    api.add_resource(University, '/university/<int:university_id>')  # GET, PUT, DELETE

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
