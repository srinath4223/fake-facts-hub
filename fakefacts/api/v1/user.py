from flask import jsonify, request
from flask_jwt_extended import jwt_required

from fakefacts.api.v1 import V1FlaskView
from fakefacts.blueprints.user.models import User
from fakefacts.blueprints.user.schemas import users_schema, registration_schema


class UserView(V1FlaskView):
    @jwt_required
    def index(self):
        users = User.query.all()

        response = {
            'data': users_schema.dump(users).data
        }

        return jsonify(response), 200

    def post(self):
        json_data = request.get_json()

        if not json_data:
            response = jsonify({'error': 'Invalid input'})

            return response, 400

        data, errors = registration_schema.load(json_data)

        if errors:
            response = {
                'error': errors
            }

            return jsonify(response), 422

        user = User()
        user.email = data.get('email')
        user.username = data.get('username')
        user.password = User.encrypt_password(data.get('password'))
        user.save()

        return jsonify(data), 200
