from db import db


class User(db.Model):

    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String)
    user_password = db.Column(db.String)
    public_id = db.Column(db.String)

    person_id_fk = db.Column(db.Integer, db.ForeignKey("person.person_id"))

    person = db.relationship('Person', backref='user_person',
                             single_parent=True, cascade="all,delete-orphan")

    user_type_fk = db.Column(db.Integer, db.ForeignKey("user.user_type_fk"))

    def __init__(self, id, username, password, user_type, person_id, public_id):
        self.user_id = id
        self.user_name = username
        self.user_password = password
        self.public_id = public_id
        self.user_type_fk = user_type
        self.person_id_fk = person_id

    @classmethod
    def get_user_by_username(self, username):
        user_ = User.query.filter_by(user_name=username).first()
        return user_

    @staticmethod
    def registrar(self):
        try:
            db.session.add(self)
            db.session.commit()
            return (True, 'Usuario creado')
        except Exception as e:
            print('Error al guardar usuario', e)
            return (False, 'Error al guardar usuario')

    @staticmethod
    def get_user_by_public_id(self, publicid):
        _user = User.query.filter(public_id=publicid)
        return _user
