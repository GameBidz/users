from app.models.user_model import User
from app.config.database import create_connection
from dotenv import load_dotenv
import os
from bson.objectid import ObjectId

load_dotenv()

DB_NAME = os.environ['DATABASE_NAME']

class UserRepository:

    def create_user(self, username:str, email:str, password:str):
        new_user = User(username=username, email=email, password=password)
        client  = create_connection()

        #Iniciar una sesión
        with client.start_session() as session:
            #Iniciar la transacción
            session.start_transaction()

            #Obtener la coleccion users
            db = client[DB_NAME]
            users = db['users']

            #Insertar el nuevo usuario
            user = users.insert_one(new_user.to_dict(), session=session).inserted_id

            #Confirmar la transacción
            session.commit_transaction()

            #Cerrar la conexión
            client.close()

            return user
    

    def get_user_by_email(self, email:str):
        client = create_connection()
        db = client[DB_NAME]
        users = db['users']
        user = users.find_one({"email": email})
        return user

    def edit_user(self, id: str,  user: User):
        client = create_connection()
        db = client[DB_NAME]
        users = db['users']

        with client.start_session() as session:
            session.start_transaction()
            user = users.update_one({"_id": ObjectId(id)}, {"$set" : user.to_dict()})
            session.commit_transaction()
                
        client.close()