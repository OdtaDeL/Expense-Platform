from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Auth Service Running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


class User(BaseModel):
    username: str
    password: str


@app.post("/register")
def register(user: User):
    return {
        "message": f"User {user.username} registered successfully"
    }


@app.post("/login")
def login(user: User):
    return {
        "message": f"User {user.username} logged in successfully"
    }
