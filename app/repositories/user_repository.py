from models.user_model import User
from config.database import create_connection

class UserRepository:

    def create_user(self, username:str, email:str, password:str):
        
        new_user = User(username=username, email=email, password=password)
    
    def get_user_by_email(self, email:str):
        pass

    def edit_user(self, user: User):
        pass
