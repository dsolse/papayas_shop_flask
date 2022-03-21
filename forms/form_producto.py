from flask_wtf import FlaskForm
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import PasswordField, StringField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError

class ProdcuctoForm(FlaskForm):
	nombre =StringField("nombre", validators=[InputRequired()])
	calidad =IntegerField("calidad", validators=[InputRequired()])
	precio = IntegerField("precio", validators=[InputRequired()])
	submit = SubmitField("Submit")

	def validate_calidad(self, calidad):
		calidad_number = calidad.data
		if calidad_number < 0 or calidad_number > 10:
			raise ValidationError("No existen calidades negativas ni mayores a 10")

	def validate_precio(self, precio):
		precio_number = precio.data
		if precio_number < 0:
			print("errot")
			raise ValidationError("No existen precio negativos: Pendejo")	