from fastapi import APIRouter, status 
from typing import Optional
from pydantic import BaseModel, Field
from enum import Enum

router = APIRouter(prefix="/supplier")

class Company(Enum):
    name: str
    siret: str


class Contact(BaseModel):
    lastname: str
    firstname: str
    email: str
    phone: str


class Supplier(BaseModel):
    name: Company
    contact: Contact

@router.get("/{supplier_id}")
def read_supplier(user_id):
    return user_id

@router.post("")
def post(data:Supplier):
    return data



