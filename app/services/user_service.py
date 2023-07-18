from repositories.user_repository import UserRepository
from flask_bcrypt import generate_password_hash

class UserService:
    def __init__(self) -> None:
        self.user_repository = UserRepository()

    def register_user(self, username, email, password):

        #Validacion de usuario existente
        if self.user_repository.get_user_by_email(email):
            return None
        if self.user_repository.get_user_by_username(username):
            return None
  
        #Encriptar contraseña
        hashed_password = generate_password_hash(password).decode('utf-8')

        #Crear el nuevo usuario
        user = self.user_repository.create_user(username, email, hashed_password)

        return user


