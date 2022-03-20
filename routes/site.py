from flask import Blueprint
from flask.templating import render_template
from flask_login import login_required, current_user

site = Blueprint("site", __name__, url_prefix="/site")

@site.route("/")
@login_required
def home():
	return render_template("home.html", user=current_user)

@site.route("/compras")
def compras():
	return "Compras"

@site.route("/producto")
def producto():
	return "Compras"

@site.route("/profile")
def profile():
	return "Compras"

@site.route("/manage_user")
def manage_user():
	return "manage_user"
