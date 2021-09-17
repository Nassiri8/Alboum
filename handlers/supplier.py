from fastapi import APIRouter, status 
from typing import Optional
from pydantic import BaseModel, Field
from enum import Enum

router = APIRouter(prefix="/supplier")

class Supplier(BaseModel):
    name:str
    phone:str
    



