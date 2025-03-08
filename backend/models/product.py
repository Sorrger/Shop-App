from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

class Product(BaseModel):
    id: Optional[str] = Field(alias="_id")
    name: str
    photo_url: Optional[str] = None
    description: Optional[str] = None
    price: float
    producer_id: str

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
