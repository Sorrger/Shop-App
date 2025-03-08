from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from bson import ObjectId

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    producer_id: str
    specifications: Optional[Dict[str, Any]] = None

class CreateProduct(ProductBase):
    pass

class Product(ProductBase):
    id: str = Field(alias="_id") 

    class Config:
        from_attributes = True
