from flask_wtf import FlaskForm
from wtforms.fields.simple import PasswordField, StringField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError

from models.usuarios import Usuarios

class RegisterForm(FlaskForm):
	nombre = StringField("Nombre user", 
		validators=[
		InputRequired(),
		Length(min=2, max=10)
		]
		)
	apellido = StringField("apellido user", 
		validators=[
		InputRequired(),
		Length(min=2, max=10)
		]
		)

	password =  PasswordField(
		"Password",
		validators= [
			InputRequired(),
			Length(min=2, max=10)
		]
		)

	submit = SubmitField("Submit")

	def validate_nombre(self, nombre):
		nombre_data = nombre.data
		user = Usuarios.query.filter_by(nombre=nombre_data).first()
		if user:
			raise ValidationError("User exists")


class LoginForm(FlaskForm):
	nombre = StringField("Nombre user", 
		validators=[
		InputRequired(),
		Length(min=2, max=10)
		]
		)

	password =  PasswordField(
		"Password",
		validators= [
			InputRequired(),
			Length(min=2, max=10)
		]
		)

	submit = SubmitField("Submit")

