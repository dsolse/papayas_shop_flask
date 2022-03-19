from utilidades.db import db

class Productos(db.Model): # type: ignore
	"""
	Campos de productos:
		id : int
		nombre : str
		pais : str
		calidad : int
		precio : int
	"""
	pass