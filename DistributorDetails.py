from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

users = {'admin_head' : {'password' : 'abc', 'role' : 'IT_Admin', 'isAdmin' : 'Y'}}

class Login(Resource):
    def post(self, user_ID):
        args = parser.parse_args()
        if user_ID in users:
            print(user_ID)
            if users[user_ID]['password'] == args['password']:
                return users[user_ID]['isAdmin']
        abort(404, message='User_ID {} or Password is invalid'.format(user_ID))

api.add_resource(Login, '/login/<string:user_ID>')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000')