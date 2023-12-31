from api.models.user import User
from api.models.person import Person
import uuid
import jwt
import datetime
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash


class UserService:

    def validate_credentials(self, username, password: str):

        if not username or not password:
            raise Exception(
                f"El campo usuario y contraseña son obligatorio y no puede estar vacío.")

        user_ = User.get_user_by_username(username)

        if (not user_):
            return {
                'error': 'Usuario no existe.'
            }, 401

        # Si el usuario no existe debe retornar 404

        if not check_password_hash(user_.user_password, password):
            return {
                'error': 'Contraseña invalida.'
            }, 401

        token = UserService.generate_token(user_.public_id)
        return {
            'public_id': user_.public_id,
            'user_type': user_.user_type.user_type_name,
            'email': user_.user_name,
            'full_name': user_.person.person_first_name + ' ' + user_.person.person_last_name,
            'token': token}, 200

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
        password = str(data['password'])
        username = data['username']

        hashed_password = generate_password_hash(password, method='sha256')

        # hashed_password = generate_password_hash(
        #     data['password'], method='scrypt')
        password = hashed_password

        person_new = Person(document=document, first_name=first_name,
                            last_name=last_name, type_document=type_document)

        public_uuid = str(uuid.uuid4())
        user_new = User(None, username=username,
                        password=password, user_type_id=1,
                        person_id=person_new.person_id,
                        public_id=public_uuid)

        user_new.person = person_new

        isRegister = User.registrar(user_new)
        if (not isRegister[0]):
            return {
                'error': 'Error creando el usuario.'
            }, 401
            
        return {
            'public_id': user_new.public_id,
            'user_type': user_new.user_type.user_type_name,
            'email': user_new.user_name,
            'full_name': user_new.person.person_first_name + ' ' + user_new.person.person_last_name,
            'user_id': user_new.user_id
            }, 201
        

    @staticmethod
    def generate_token(public_id):

        payload = {
            'public_id': public_id,
            'iat': datetime.datetime.utcnow(),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=120)
        }

        token = jwt.encode(payload, current_app.config['SECRET_KEY'])

        return token
