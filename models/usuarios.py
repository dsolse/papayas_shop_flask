from flask_login.mixins import UserMixin
from utilidades.db import db

class Usuarios(db.Model, UserMixin): # type: ignore
	"""
	Campos de usuarios:	
		id : int
		nombre : str
		apellido : str
		password : str
	"""
	# Campos
	id = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String(50))
	apellido = db.Column(db.String(50))
	password = db.Column(db.String(200))
	rank = db.Column(db.Boolean)
	
	# constructor para meter esos campos
	def __init__(self, nombre, apellido, password, rank) -> None:
		self.nombre = nombre
		self.apellido = apellido
		self.password = password
		self.rank = rank
