from api.models.user import User
from api.models.mentoring import Mentoring
from api.models.mentoring_user import MentoringUser
from flask import current_app


class MentoringService():

    def get_all_mentoring_available(self):
        mentorings = Mentoring.mentorings_by_avaliable()

        response = []

        for mention in mentorings:
            response.append({'classroom': mention.ment_classroom,
                             'schedule': mention.ment_schedules,
                             'name': mention.ment_name,
                             'mentor': f'{mention.user.person.person_first_name} {mention.user.person.person_last_name}',
                             'id': mention.ment_id, })

        return {'mentoring': response}, 200

    def create_mentoring(self, data):

        required_fields = ['classroom', 'mentor_id',
                           'schedule', 'name']
        for field in required_fields:
            if field not in data or not data[field]:
                return {
                    'error': f"El campo '{field}' es obligatorio y no puede estar vacío."
                }, 400

        classroom = data['classroom']
        mentor = data['mentor_id']
        schedule = data['schedule']
        name_mentoring = data['name']

        new_mentoring = Mentoring(
            classroom=classroom, mentor_id=mentor, status=1, schedule=schedule, name=name_mentoring)

        isRegistered = Mentoring.create_mentoring(new_mentoring)

        if (not isRegistered[0]):
            raise Exception(isRegistered[1])

        return {'classroom': new_mentoring.ment_classroom,
                'schedule': new_mentoring.ment_schedules,
                'name': new_mentoring.ment_name,
                'mentor': f'{new_mentoring.user.person.person_first_name} {new_mentoring.user.person.person_last_name}',
                'id': new_mentoring.ment_id, }, 200

    def get_all_mentoring_by_user(self, id_user):
        mentorings = []
        if (not id_user):
            return {
                'error': 'El campo id usuario no esta presente.'
            }, 400

        user = User.get_user_by_public_id(id_user)
        if (user.user_type_fk == 2):  # Valida si es mentor
            mentorings = Mentoring.mentorings_by_user_mentor(user.user_id)
        else:
            mentorings = Mentoring.mentorings_by_user_student(user.user_id)

        response = []

        for mention in mentorings:
            response.append({'classroom': mention.ment_classroom,
                             'schedule': mention.ment_schedules,
                             'name': mention.ment_name,
                             'mentor': f'{mention.user.person.person_first_name} {mention.user.person.person_last_name}',
                             'id': mention.ment_id, })

        return {'mentoring': response}, 200

    def enroll_mentoring(self, data):

        required_fields = ['id_public', 'ment_id']
        for field in required_fields:
            if field not in data or not data[field]:
                return {
                    'error': f"El campo '{field}' es obligatorio y no puede estar vacío."
                }, 400

        id_user_student = data['id_public']
        id_ment = data['ment_id']

        _user = User.get_user_by_public_id(id_user_student)
        if (not _user):
            return {
                'error': 'Usuario no existe.'
            }, 400

        _ment = Mentoring.mentoring_by_id(id=id_ment)
        if (not _ment):
            return {
                'error': 'Mentoria no existe.'
            }, 400

        isRegistered = MentoringUser(id=None, user_id=_user.user_id,
                                     mentoring_id=_ment.ment_id).create_mentoring_user()

        if (not isRegistered[0]):
            raise Exception(isRegistered[1])

        return {'message': isRegistered[1]}, 200