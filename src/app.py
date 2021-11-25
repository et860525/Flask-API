from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, reqparse, Api, abort, fields, marshal_with
from requests.api import delete

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

db.create_all()

parser = reqparse.RequestParser()
parser.add_argument("username", type=str, help="Username is required", required=True)
parser.add_argument("email", type=str, help="Email is required", required=True)

user_update = reqparse.RequestParser()
user_update.add_argument("username", type=str)
user_update.add_argument("email", type=str)

resource_fields = {
	'id': fields.Integer,
	'username': fields.String,
	'email': fields.String
}

class User(Resource):
	@marshal_with(resource_fields)
	def get(self, user_id):
		result = UserModel.query.filter_by(id=user_id).first()
		if not result:
			abort(404, message="User not exist...")
		return result

	@marshal_with(resource_fields)
	def put(self, user_id):
		args = parser.parse_args()
		result = UserModel.query.filter_by(id=user_id).first()
		if result:
			abort(409, message="User id Taken.")

		new_user = UserModel(id=user_id, username=args['username'], email=args['email'])
		db.session.add(new_user)
		db.session.commit()
		return new_user, 201

	# @marshal_with(resource_fields)
	def delete(self, user_id):
		result = UserModel.query.filter_by(id=user_id).first()
		if not result:
			abort(404, message="User not exist...")
		db.session.delete(result)
		db.session.commit()
		return {'message': 'user_id %r is been remove...' % user_id}, 201

class UserList(Resource):
	@marshal_with(resource_fields)
	def get(self):
		results = UserModel.query.all()
		return results, 201

api.add_resource(UserList, '/users/')
api.add_resource(User, '/users/<int:user_id>')

if __name__ == '__main__':
	app.run(debug=True)