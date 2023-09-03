from flask import Flask
from api.routes.user_route import users_bp
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# settings
app.secret_key = ''
app.config["SQLALCHEMY_DATABASE_URI"] = ''
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# no cache
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


app.register_blueprint(users_bp)

