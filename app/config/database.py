from pymongo.mongo_client import MongoClient
import os
from dotenv import load_dotenv

#Cargar variables de entorno
load_dotenv()

DB_USER = os.environ['DATABASE_USER']
DB_PASS = os.environ['DATABASE_PASS']
DB_HOST = os.environ['DATABASE_HOST']
DB_NAME = os.environ['DATABASE_NAME']

def create_connection() -> MongoClient:
    
    uri  = f'mongodb+srv://{DB_USER}:{DB_PASS}@{DB_HOST}/?retryWrites=true&w=majority'

    #Crear cliente Mongo y conectar DB
    client = MongoClient(uri)

    #Probar la conexión
    try:
        client.admin.command('ping')
        print("Conexión exitosa!!!")
        return client
    
    except Exception as e:
        print(e)
        return
