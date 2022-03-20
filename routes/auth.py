from flask import Blueprint, render_template
from models.usuarios import Usuarios
from models.compras import Compras
from models.productos import Productos
from utilidades.db import db

auth = Blueprint("auth", __name__)

@auth.route("/")
def home():
	user = Usuarios("David", "solis", "kkajdhk")
	prod = Productos("Papaya premium", 8, 30)

	db.session.add(user)
	db.session.add(prod)
	db.session.commit()
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
