from utilidades.db import db

class Productos(db.Model): # type: ignore
	"""
	Campos de productos:
		id : int
		nombre : str
		calidad : int
		precio : int
	"""
	# Campos
	id = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String(50))
	calidad =  db.Column(db.Integer)
	precio = db.Column(db.Integer)
	
	# constructor para meter esos campos
	def __init__(self, nombre, producto, cantidad, precio) -> None:
		self.nombre = nombre
		self.cantidad = cantidad
		self.precio = precio


