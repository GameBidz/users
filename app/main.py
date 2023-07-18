from fastapi import FastAPI
from models.user_model import User
from controllers.user_controller import UserController

app = FastAPI()

@app.get("/")
async def hello():
    return {"message" : "Hello World"}

@app.post("/register", status_code=201)
async def register_user(user: User):
    return UserController().register_user(user)