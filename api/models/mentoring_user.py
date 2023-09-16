from db import db


class MentoringUser(db.Model):

    __tablename__ = 'mentoring_user'

    id = db.Column(db.Integer, primary_key=True)
    ment_id = db.Column(db.Integer, db.ForeignKey("mentoring.ment_id"))

    mentoring = db.relationship('Mentoring', backref='mento_user',
                                single_parent=True, cascade="all,delete-orphan")

    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"))

    user = db.relationship('User', backref='user_ment',
                           single_parent=True, cascade="all,delete-orphan")

    def __init__(self, id, user_id, mentoring_id):
        self.id = id
        self.user_id = user_id
        self.ment_id = mentoring_id

    def create_mentoring_user(self,):
        try:
            db.session.add(self)
            db.session.commit()
            return (True, 'Se realizo la matricula exitosamente.')
        except Exception as e:
            print('Error matriculando al estudiante', e)
            return (False, 'Error matriculando al estudiante')
