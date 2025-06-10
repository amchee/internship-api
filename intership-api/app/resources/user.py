from flask_restful import Resource, reqparse
from app.models.user import UserModel
from flask_jwt_extended import create_access_token

_user_parser = reqparse.RequestParser()
_user_parser.add_argument("username", type=str, required=True, help="Username is required")
_user_parser.add_argument("password", type=str, required=True, help="Password is required")


class UserRegister(Resource):
    def post(self):
        data = _user_parser.parse_args()

        if UserModel.find_by_username(data["username"]):
            return {"message": "User already exists."}, 400

        user = UserModel(username=data["username"], password=data["password"])
        user.save_to_db()

        return {"message": "User created successfully."}, 201



class UserLogin(Resource):
    def post(self):
        data = _user_parser.parse_args()
        user = UserModel.find_by_username(data["username"])

        if user and user.password == data["password"]:
            access_token = create_access_token(identity=str(user.id))

            return {"access_token": access_token}, 200

        return {"message": "Invalid credentials"}, 401
