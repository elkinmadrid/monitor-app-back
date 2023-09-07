from db import db


class UserType(db.Model):

    __tablename__ = 'user_type'

    user_type_id = db.Column(db.Integer, primary_key=True)
    user_type_name = db.Column(db.String)
    user_type_description = db.Column(db.String)

    user = db.relationship('User', uselist=False,
                           backref="user_type_user", cascade="all, delete-orphan", single_parent=True)
    
    def __init__(self, type_id, type_name, type_descripcion):
        self.user_type_id = type_id
        self.user_type_name = type_name
        self.user_type_description = type_descripcion

