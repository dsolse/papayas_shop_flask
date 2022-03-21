from utilidades.db import db

class Compras(db.Model): # type: ignore
	"""
	Campos en compras:
		id : str
		user : int
		producto : int
		cantidad : int
	"""
	id = db.Column(db.Integer, primary_key=True)
	user = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
	producto =  db.Column(db.Integer, db.ForeignKey('productos.id'))
	cantidad =db.Column(db.Integer)
	
	def __init__(self, user, producto, cantidad) -> None:
		self.user = user
		self.producto = producto
		self.cantidad = cantidad
		
