from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)

@auth.route("/")
def home():
	return render_template("auth/home.html")

@auth.route('/login', methods=["POST", "GET"])
def login():
	return render_template("auth/login.html")

@auth.route('/register', methods=["POST", "GET"])
def register():
	return render_template("auth/register.html")

@auth.route('/login', methods=["POST", "GET"])
def logout():
	return "deslogearse"
