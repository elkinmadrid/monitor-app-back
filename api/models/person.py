from db import db

class Person(db.Model):

    __tablename__ = 'person'

    person_id = db.Column(db.Integer, primary_key=True)
    person_first_name = db.Column(db.String)
    person_last_name = db.Column(db.String)
    person_type_document = db.Column(db.String)
    person_document = db.Column(db.String)

    user = db.relationship('User',uselist=False,
    backref="person_user",cascade="all, delete-orphan",single_parent=True)

    def __init__(self, first_name, last_name, type_document, document):
        self.person_first_name = first_name
        self.person_last_name = last_name
        self.person_type_document = type_document
        self.person_document = document
