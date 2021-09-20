from app.auth.v1.models.user_models import UserModels
from flask import request
from flask_restful import Resource
from flask_restful.reqparse import RequestParser

parser = RequestParser()

parser.add_argument("username", type=str,required=True,
 help="Please input your name")

class User(Resource):
    '''
    User endpoints
    '''

    def post(self):
        '''
        Register a user endpoint
        '''
        args = parser.parse_args()
        args = request.get_json()
        username = args["username"]
        password = args["password"]
        confirm_password = args["confirm_password"]
        work = args["work"]
        worktimer = args["worktimer"]
        breaktimer = args["breaktimer"]

        newUser = UserModels(username,password,confirm_password,work,worktimer,breaktimer)
        newUser.save_user()

        return{
            "message":"User registered successfully",
            "user":newUser.__dict__
        }, 201

    def get(self):
        pass