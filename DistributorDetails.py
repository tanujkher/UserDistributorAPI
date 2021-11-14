from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

parser.add_argument('password', type=str, help='Enter your password string')
parser.add_argument('role', type=str, help='Enter your post')
parser.add_argument('isAdmin', type=str, help="Enter Y or N", choices=['Y', 'N'])

users = {'admin_head' : {'password' : 'abc', 'role' : 'IT_Admin', 'isAdmin' : 'Y'}}
dis = {}

class Login(Resource):
    def post(self, user_ID):
        args = parser.parse_args()
        if user_ID in users:
            print(user_ID)
            if users[user_ID]['password'] == args['password']:
                return users[user_ID]['isAdmin']
        abort(404, message='User_ID {} or Password is invalid'.format(user_ID))

api.add_resource(Login, '/login/<string:user_ID>')

class User(Resource):
    def get(self, user_ID=None):
        if user_ID == None:
            return users
        if user_ID in users:
            return users[user_ID]
        abort(404, message='User {} doesn\'t exist'.format(user_ID))
    def post(self, user_ID):
        if user_ID not in users:
            args = parser.parse_args()
            users[user_ID] = args #{'password' : args['password'], 'role' : args['role'], 'isAdmin' : args['isAdmin']}
            print(users)
            return 'User_ID {} created'.format(user_ID)
        abort(404, message='User {} already exists'.format(user_ID)) 
    def put(self, user_ID):
        if user_ID in users:
            users[user_ID] = parser.parse_args()
            return users[user_ID]
        abort(404, message='User {} not in users'.format(user_ID))   
    def delete(self, user_ID):
        if user_ID in users:
            del users[user_ID]
            return "User {} deleted".format(user_ID)
        abort(404, message='User {} doesn\'t exist'.format(user_ID))

api.add_resource(User, '/user/<string:user_ID>', '/user')

par = reqparse.RequestParser()
par.add_argument('contract_date', type=str, help='Enter date')
par.add_argument('product_name', type=str, help='Enter product name')

class Distributor(Resource):
    def get(self, dis_ID=None):
        if dis_ID==None:
            return dis
        if dis_ID in dis:
            return dis[dis_ID]
        abort(404, message='Distributor {} doesn\'t exist'.format(dis_ID))
    def post(self, dis_ID):
        if dis_ID not in dis:
            args = par.parse_args()
            dis[dis_ID] = args
            return 'Distributor {} added'.format(dis_ID)
        abort(404, message='Distributor {} is already present'.format(dis_ID))
    def put(self, dis_ID):
        if dis_ID in dis:
            args = par.parse_args()
            dis[dis_ID] = args
            return dis[dis_ID]
        abort(404, message='Distributor {} doesn\'t exist'.format(dis_ID))
    def delete(self, dis_ID):
        if dis_ID in dis:
            del dis[dis_ID]
            return 'Distributor {} deleted'.format(dis_ID)
        abort(404, message='Distributor {} doesn\'t exist'.format(dis_ID))

api.add_resource(Distributor, '/dis/<string:dis_ID>', '/dis')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000')