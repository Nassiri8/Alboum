from fastapi import APIRouter, status 
from typing import Optional
from pydantic import BaseModel, Field
from enum import Enum

router = APIRouter(prefix="/item")

class Categorie(str, Enum):
    mangas = "mangas"
    comics = "comics"
    figurines = "figurines"
    goodies = "goodies"

class Item(BaseModel):
    name:str = Field(None, title="Article name", max_length=255, example="Sac Yves-Saint-Laurent")
    type: Categorie = Field(None, title="Type of Product", example = "bags")
    price: float = Field(None, title="Article Price", example=499.99)
    is_offer : Optional[bool] = None

@router.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@router.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@router.post("/item", status_code=status.HTTP_201_CREATED)
def post_item(item: Item):
    return {"item_name": item.name, "price": item.price}