from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from routes.auth import auth
from routes.site import site
from utilidades.db import db
from utilidades.login import login_manager

app = Flask(__name__)

app.config.from_object("config.BaseConfig")

# Add blueprints
app.register_blueprint(auth)
app.register_blueprint(site)

# Add services e inicializarlos
SQLAlchemy(app)
Bcrypt(app)
login_manager.init_app(app)

with app.app_context():
	db.create_all()
