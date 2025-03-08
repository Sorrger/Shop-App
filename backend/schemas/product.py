from pydantic import BaseModel, Field
from typing import Optional

class ProductBase(BaseModel):
    name: str
    photo_url: Optional[str] = None
    description: Optional[str] = None
    price: float
    producer_id: str

class CreateProduct(ProductBase):
    pass

class Product(ProductBase):
    id: str = Field(alias="_id")

    class Config:
        populate_by_name = True
