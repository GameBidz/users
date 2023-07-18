from fastapi import FastAPI, Body
from models.user_model import User
from controllers.user_controller import UserController
from typing import Annotated

app = FastAPI()

@app.get("/")
async def hello():
    return {"message" : "Hello World"}

@app.post("/register", status_code=201)
async def register_user(user: User):
    return UserController().register_user(user)

@app.post("/login", status_code=200)
async def login(username: Annotated[str, Body()], password: Annotated[str, Body()]):
    return UserController().login(username, password)