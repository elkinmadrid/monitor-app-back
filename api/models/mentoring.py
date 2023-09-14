from db import db


class Mentoring(db.Model):
    __tablename__ = 'mentoring'

    ment_id = db.Column(db.Integer, primary_key=True)
    ment_classroom = db.Column(db.String)
    ment_status = db.Column(db.Integer)
    ment_schedules = db.Column(db.String)
    ment_name = db.Column(db.String)

    ment_schedules_id_fk = db.Column(db.Integer)

    ment_user_id_mentor = db.Column(db.Integer, db.ForeignKey("user.user_id"))

    user = db.relationship('User', backref='user_mentor',
                             single_parent=True, cascade="all,delete-orphan")

    def __init__(self, classroom, status, schedule_id, mentor_id, schedule, name):

        self.ment_classroom = classroom
        self.ment_status = status
        self.ment_schedules = schedule
        self.ment_schedules_id_fk = schedule_id
        self.ment_user_id_mentor = mentor_id
        self.ment_name = name

    def mentorings_by_avaliable():

        try: 
            mentorings = Mentoring.query.filter_by(ment_status=1)

            return mentorings

        except Exception as e:
            print('Error al obteniendo mentorias disponibles', e)
            return (False, 'Error al obteniendo mentorias disponibles')
        


        
    def create_mentoring(self,):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            print('Error al guardar mentoria', e)
            return (False, 'Error al guardar mentoria')
        