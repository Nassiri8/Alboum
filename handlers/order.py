from fastapi import APIRouter, status 
from typing import Optional
from pydantic import BaseModel, Field
from enum import Enum

router = APIRouter(prefix="/order")

class Order(BaseModel):
    number:str = Field(None, title="order number", max_length=255, example="12334323")
    user_id: int  = Field(None, title="id client", example = "1")

@router.get("/{order_id}")
def read_order(order_id: int, q: Optional[str] = None):
    return {"order_id": order_id, "q": q}

