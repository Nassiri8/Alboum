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

@router.get("/{user_id}")
def read_user(user_id):
    return user_id

@router.get("")
def read_all_users():
    user = {}
    return user

@router.post("")
def post(data:User):
    return data