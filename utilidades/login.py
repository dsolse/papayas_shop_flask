from flask_login import LoginManager

from models.usuarios import Usuarios

login_manager = LoginManager()
login_manager.login_view = "auth.login" # type: ignore
# Implementas login

@login_manager.user_loader
def load_user(user_id):
	user = Usuarios.query.get(user_id)
	return user
