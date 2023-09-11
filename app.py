from flask import Flask
from api.routes.user_route import users_bp
from api.routes.mentorias_route import monitoria_bp
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)


app.config['SECRET_KEY'] = os.environ['JWT_SECRETKEY']

# settings

host = os.environ['HOST']
nombre_bd = os.environ['NAME_BD']
nombre_usuario = os.environ['USERNAME']
password = os.environ['PASSWORD']

app.config["SQLALCHEMY_DATABASE_URI"] = f'postgresql://{nombre_usuario}:{password}@{host}:5432/{nombre_bd}'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# no cache
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


app.register_blueprint(users_bp)
app.register_blueprint(monitoria_bp)
