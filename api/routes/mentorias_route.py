from jwt_impl import token_required
from flask import Blueprint, jsonify, make_response, request
from api.services.mentoring_service import MentoringService

monitoria_bp = Blueprint('mentoring', __name__)

mentoring_service = MentoringService()


@monitoria_bp.route('/api/mentoring/avaliable', methods=['GET'])
@token_required
def list_monitorias_disponible(self):

    try:
        _mentorings = mentoring_service.get_all_mentoring_available()
        return make_response(jsonify(_mentorings[0]), _mentorings[1])
    except Exception as e:
        return make_response(jsonify({'error': e.args[0]}), 500)


@monitoria_bp.route('/api/mentoring/create', methods=['POST'])
@token_required
def create_mentoring(self):
    try:

        body = request.get_json()

        _mentoring = mentoring_service.create_mentoring(data=body)

        return make_response(jsonify(_mentoring[0]), _mentoring[1])

    except Exception as e:
        return make_response(jsonify({'error': e.args[0]}), 500)


@monitoria_bp.route('/api/mentoring/user/<id>', methods=['GET'])
@token_required
def list_monitorias_por_usuario(self, id):

    try:
        print(id)
        _mentorings = mentoring_service.get_all_mentoring_by_user(id)
        return make_response(jsonify(_mentorings[0]), _mentorings[1])
    except Exception as e:
        return make_response(jsonify({'error': e.args[0]}), 500)


@monitoria_bp.route('/api/mentoring/enroll', methods=['POST'])
@token_required
def enroll_student_mentoring():
    try:
        body = request.get_json()

        enroll = mentoring_service.enroll_mentoring(body)

        return make_response(jsonify(enroll[0]), enroll[1])
    except Exception as e:
        return make_response(jsonify({'error': e.args[0]}), 500)
