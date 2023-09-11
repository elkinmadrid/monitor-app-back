from api.models.user import User
from api.models.mentoring import Mentoring
from flask import current_app


class MentoringService():

    def get_all_mentoring_available(self):
        mentorings = Mentoring.mentorings_by_avaliable()

        response = []

        for mention in mentorings:
            response.append({'classroom': mention.ment_classroom,
                             'schedule': mention.ment_schedules,
                             'mentor': f'{mention.user.person.person_first_name} {mention.user.person.person_last_name}',
                             'id': mention.ment_id, })

        return {'mentoring': response}, 200

    def create_mentoring(self, data):

        classroom = data['classroom']
        mentor = data['mentor_id']
        schedule = data['schedule']

        new_mentoring = Mentoring(
            classroom=classroom, schedule_id=None, mentor_id=mentor, status=1, schedule=schedule)

        Mentoring.create_mentoring(new_mentoring)

        return {'classroom': new_mentoring.ment_classroom,
                'schedule': new_mentoring.ment_schedules,
                'mentor': f'{new_mentoring.user.person.person_first_name} {new_mentoring.user.person.person_last_name}',
                'id': new_mentoring.ment_id, }, 200
