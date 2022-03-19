from flask import Blueprint

auth = Blueprint("auth", __name__, url_prefix="/auth")

@auth.route("/")
def home():
	return "Auth app"

@auth.route('/login', methods=["POST", "GET"])
def login():
	return "Logearse"

@auth.route('/register', methods=["POST", "GET"])
def register():
	return "Registrarse"

@auth.route('/login', methods=["POST", "GET"])
def logout():
	return "deslogearse"
