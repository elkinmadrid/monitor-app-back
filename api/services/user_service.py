from api.models.user import User
from api.models.person import Person
import uuid
import jwt
import datetime
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash


class UserService:

    def validate_credentials(self, username, password):

        if not username or not password:
            raise Exception(
                f"El campo usuario y contraseña son obligatorio y no puede estar vacío.")

        user_ = User.get_user_by_username(username)

        if not check_password_hash(user_.user_password, password):
            return {
                'error': 'Invalid password'
            }, 401

        token = UserService.generate_token(user_.public_id)
        return {'token': token}, 200

    def registrar_estudiante(self, data):

        required_fields = ['document', 'type_document',
                           'first_name', 'last_name', 'password', 'username']
        for field in required_fields:
            if field not in data or not data[field]:
                raise Exception(
                    f"El campo '{field}' es obligatorio y no puede estar vacío.")

        # Persona
        document = data['document']
        type_document = data['type_document']
        first_name = data['first_name']
        last_name = data['last_name']

        # User
        password = data['password']
        username = data['username']

        hashed_password = generate_password_hash(
            data['password'], method='scrypt')
        password = hashed_password

        person_new = Person(document=document, first_name=first_name,
                            last_name=last_name, type_document=type_document)

        public_uuid = str(uuid.uuid4())
        user_new = User(None, username=username,
                        password=password, user_type=1,
                        person_id=person_new.person_id,
                        public_id=public_uuid)

        user_new.person = person_new

        User.registrar(user_new)

    @staticmethod
    def generate_token(public_id):

        payload = {
            'public_id': public_id,
            'iat': datetime.datetime.utcnow(),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=120)
        }

        token = jwt.encode(payload, current_app.config['SECRET_KEY'])

        return token
