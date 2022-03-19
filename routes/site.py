from flask import Blueprint

site = Blueprint("site", __name__, url_prefix="/site")

@site.route("/")
def home():
	return "home site"

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
