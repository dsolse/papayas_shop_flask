from flask_wtf import FlaskForm
from wtforms.fields.choices import SelectField
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import PasswordField, StringField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError

class ComprasForm(FlaskForm):
	producto = SelectField("Productos")
	cantidad = IntegerField("Cantidad")
	submit = SubmitField("add")

	def validate_cantidad(self, cantidad):
		if cantidad.data < 0:
			raise ValidationError("No uni menor a cero")
