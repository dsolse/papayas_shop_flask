from inspect import currentframe
from flask import Blueprint
from flask.helpers import url_for
from flask.templating import render_template
from flask_login import login_required, current_user
from werkzeug.utils import redirect
from forms.form_compra import ComprasForm
from forms.form_producto import ProdcuctoForm
from models.compras import Compras
from utilidades.db import db

from models.productos import Productos
from models.usuarios import Usuarios


def make_list(prods):
	list_prod = []
	for prod in range(1, len(prods) + 1):
		producto = prods[prod - 1]
		list_prod.append((f"{prod}", f"{producto.nombre} {producto.calidad} {producto.precio}"))
	return list_prod

site = Blueprint("site", __name__, url_prefix="/site")

@site.route("/")
@login_required
def home():
	return render_template("home.html", user=current_user)

@site.route("/compras", methods=["GET", "POST"])
@login_required
def compras():
	form = ComprasForm()
	prods = Productos.query.all()
	form.producto.choices = make_list(prods)
	if current_user.rank:
		compras = Compras.query.all()
	else:
		compras = Compras.query.filter_by(user=current_user.id)
	if form.validate_on_submit():
		prod = form.producto.data
		user = current_user.id
		cantidad = form.cantidad.data
		comp = Compras(user, prod, cantidad)
		db.session.add(comp)
		db.session.commit()
		
	return render_template("compras.html", user=current_user, form=form, compras = compras)

# admin
@site.route("/producto", methods=["POST", "GET"])
@login_required
def producto():
	# ejecuta cuando no soy admin
	if not current_user.rank:
		return redirect(url_for("site.home"))
	form = ProdcuctoForm()

	if form.validate_on_submit():
		nombre =form.nombre.data
		calidad = form.calidad.data
		precio =form.precio.data
		prod = Productos(nombre, calidad, precio)
		db.session.add(prod)
		db.session.commit()

	productos = Productos.query.all()
	return render_template("productos.html", productos = productos, user=current_user, form=form)


@site.route("/profile")
@login_required
def profile():
	return render_template("perfil.html", user=current_user)

# admin
@site.route("/manage_user")
@login_required
def manage_user():
	if not current_user.rank:
		return redirect(url_for("site.home"))
	usuarios = Usuarios.query.all()
	return render_template("manage_user.html", user=current_user, usuarios=usuarios)
