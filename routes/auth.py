from flask import Blueprint, render_template, redirect
from flask.helpers import url_for
from models.usuarios import Usuarios
from models.compras import Compras
from models.productos import Productos
from utilidades.db import db
from utilidades.bcrypt import bcrypt
from forms.form_usuarios import LoginForm, RegisterForm
from flask_login import login_user, logout_user

auth = Blueprint("auth", __name__)

@auth.route("/")
def home():
	return render_template("auth/home.html")

@auth.route('/login', methods=["POST", "GET"])
def login():
	form = LoginForm()
	# method post
	if form.validate_on_submit():
		nombre = form.nombre.data
		password = form.password.data
		user = Usuarios.query.filter_by(nombre=nombre).first()
		if user:
			if bcrypt.check_password_hash(user.password, password):
				login_user(user)
				return redirect(url_for('site.home'))
	return render_template("auth/login.html", form=form)

@auth.route('/register', methods=["POST", "GET"])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		nombre = form.nombre.data
		apellido = form.apellido.data
		passw = form.password.data
		password = bcrypt.generate_password_hash(passw)
		# no hay campos
		
		if not Usuarios.query.all():
			user = Usuarios(nombre=nombre, apellido=apellido, password=password, rank=True)
		else:
			user = Usuarios(nombre=nombre, apellido=apellido, password=password, rank=False)
		
		db.session.add(user)
		db.session.commit()
		return redirect(url_for('auth.login'))
	form.nombre.data = ""
	form.apellido.data = ""
	form.password.data = ""
	return render_template("auth/register.html", form=form)

@auth.route('/logout', methods=["POST", "GET"])
def logout():
	logout_user()
	return redirect(url_for("auth.home"))
