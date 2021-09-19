from fastapi import APIRouter
from typing import Optional
from pydantic import BaseModel, EmailStr

router = APIRouter(prefix="/admin")

class User(BaseModel):
    firstname:str
    lastname:str
    email: EmailStr
    phone:str
    password: str

@router.get("{user_id}")
def get_admin(user_id):
    return user_id

@router.post("")
def post(data:User):
    return data