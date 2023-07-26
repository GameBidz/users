from repositories.user_repository import UserRepository
from flask_bcrypt import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import datetime
import jwt
import os

load_dotenv()

SECRET_KEY = os.environ['SECRET_KEY']

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
    
    def login(self, username, password):

        user = self.user_repository.get_user_by_username(username)

        #validacion de usuario existente
        if user:
            pass_candidate = password
            if check_password_hash(user['password'], pass_candidate):
                token = self.generate_token(user['username'])
                return {"token": token}
        
        #Usuario no existe o credenciales invalidas
        return None
    
    def generate_token(self, username: str) -> str:
        payload = {
            'username': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }

        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return token



