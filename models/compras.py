from utilidades.db import db

class Compras(db.Model): # type: ignore
	"""
	Campos en compras:
		id : str
		user : int
		producto : int
		cantidad : int
	"""
	pass