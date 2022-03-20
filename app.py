from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from routes.auth import auth
from utilidades.db import db

app = Flask(__name__)

app.config.from_object("config.BaseConfig")

# Add blueprints
app.register_blueprint(auth)
# Add services e inicializarlos
SQLAlchemy(app)

with app.app_context():
	db.create_all()
