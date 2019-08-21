from flask import jsonify, request
from flask_classful import route
from flask_jwt_extended import (
    jwt_required,
    current_user
)

from lib.flask_pusher import pusher
from fakefacts.extensions import db
from fakefacts.api.v1 import V1FlaskView
from fakefacts.blueprints.user.models import User
from fakefacts.blueprints.facts.models import Fact
from fakefacts.blueprints.facts.schemas import (
    add_fact_schema,
    facts_schema
)


class FactsView(V1FlaskView):
    @jwt_required
    def index(self):
        response = {
            'error': {
                'message': 'Username does not exist.'
            }
        }

        username = request.args.get('username', default=None, type=str)

        if username is None:
            return jsonify(response), 400

        user = User.find_by_identity(username)

        if user is None:
            return jsonify(response), 404

        editable = False
        if username == current_user.username:
            editable = True

        facts = Fact.query.filter_by(
            user_id=user.id).order_by(Fact.created_on.desc())

        response = {
             'data': facts_schema.dump(facts).data,
             'editable': editable
        }

        return jsonify(response), 200

    @jwt_required
    def post(self):
        json_data = request.get_json()

        if not json_data:
            response = jsonify({'error': 'Invalid input'})

            return response, 400

        data, errors = add_fact_schema.load(json_data)

        if errors:
            response = {
                'error': errors
            }

            return jsonify(response), 422

        fact = Fact()
        fact.user_id = current_user.id
        fact.message = data['message']
        fact.save()

        pusher.trigger('private-facts', 'new-fact',
                       {'message': fact.message,
                        'username': current_user.username})

        response = {
            'data': {
                'created_on': fact.created_on,
                'id': fact.id,
                'message': fact.message
            },
            'editable': True
        }

        return jsonify(response), 200

    @jwt_required
    def patch(self, id):
        response = {
            'error': {
                'message': 'Fact does not exist'
            }
        }

        try:
            id = int(id)
        except ValueError:
            return jsonify(response), 404

        json_data = request.get_json()

        if not json_data:
            response = {
                'error': 'Invalid input'
            }

            return jsonify(response), 400

        data, errors = add_fact_schema.load(json_data)

        if errors:
            response = {
                'error': errors
            }

            return jsonify(response), 422

        fact = Fact.query.filter_by(id=id, user_id=current_user.id) \
            .update(dict(message=data.get('message')))

        if fact == 0:
            return jsonify(response), 404

        db.session.commit()

        return jsonify(data), 200

    @jwt_required
    def delete(self, id):
        response = {
            'error': {
                'message': 'Fact does not exist'
            }
        }

        try:
            id = int(id)
        except ValueError:
            return jsonify(response), 404

        fact = Fact.query.filter_by(id=id, user_id=current_user.id).delete()

        if fact == 0:
            return jsonify(response), 404

        response = {
             'data': {
                 'id': fact
             }
        }

        db.session.commit()

        return jsonify(response), 200

    @route('/latest/', methods=['GET'])
    @jwt_required
    def latest(self):
        response = {
             'data': Fact.from_community(5),
        }

        return jsonify(response), 200
