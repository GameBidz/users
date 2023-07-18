from models.user_model import User
from services.user_service import UserService
from fastapi import HTTPException

class UserController:
    def __init__(self) -> None:
        self.user_service = UserService()

    def register_user(self, user: User):
        new_user = self.user_service.register_user(**user.model_dump())
        if new_user:
            return {"user_id": str(new_user)}
        raise HTTPException(status_code=409, detail='User alredy register')