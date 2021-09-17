from fastapi import APIRouter
from typing import Optional
from pydantic import BaseModel, EmailStr

router = APIRouter(prefix="/user")

class User(BaseModel):
    firstname:str
    lastname:str
    email: EmailStr
    phone:str
    password: str

@router.get("/user/{user_id}")
def getUserById(user_id):
    return user_id

@router.get("/users")
def getUsers():
    user = {}
    return user

@router.post("/user")
def post(data:User):
    return data