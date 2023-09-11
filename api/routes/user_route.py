from flask import Blueprint, request, jsonify, current_app, make_response

from api.services.user_service import UserService

users_bp = Blueprint('user', __name__)

user_service = UserService()

@users_bp.route('/register', methods=['POST'])
def signup_user():

    try: 
        data = request.get_json()
        response = user_service.registrar_estudiante(data)

        return make_response(jsonify(response[0]), response[1])
    except Exception as e: 
        return make_response(jsonify({'error': e.args[0]}), 500)

@users_bp.route('/login', methods=['POST'])
def login_user():
    try: 
        auth = request.get_json()

        response = user_service.validate_credentials(auth['username'], auth['password'])
    
        return make_response(jsonify(response[0]), response[1])
    except Exception as e:
        return make_response(jsonify({'error': e.args[0]}), 500)

