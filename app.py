from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from routes.auth import auth

app = Flask(__name__)

# Add blueprints
app.register_blueprint(auth)
# Add services e inicializarlos
