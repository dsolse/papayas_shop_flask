from utilidades.db import db

class Usuarios(db.Model): # type: ignore
	"""
	Campos de usuarios:	
		id : int
		nombre : str
		apellido : str
		nickname : str
		password : str
	"""
	pass