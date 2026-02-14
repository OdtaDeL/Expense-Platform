from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    username: str
    password: str

@router.post("/register")
def register(user: User):
    return {"message": f"User {user.username} registered"}

@router.post("/login")
def login(user: User):
    return {"message": f"User {user.username} logged in"}
