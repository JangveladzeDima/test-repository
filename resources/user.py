from flask_restful import Resource, reqparse
from models.USER import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank.")
    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'massage': "this username are already exists"}, 400

        create_user = UserModel(**data) # vqmni useris models abrunebs obietqts **raspakovka
        create_user.save_to_db()
        return {'massage': "User created succesfully."}, 201