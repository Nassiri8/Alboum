from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from typing import Optional
from pydantic import BaseModel, EmailStr
from database.db import engine
from sqlalchemy.sql import select
from sqlalchemy import text

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
    users = []
    with engine.connect() as conn:
        result = conn.execute(text('select * from account'))
        for row in result:
            users.append(row)
        
        users = jsonable_encoder(users)
        return JSONResponse(content=users)
    return {"message":"lol"}

@router.post("")
def post(data:User):
    return data