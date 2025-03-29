from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

class ProductBase(BaseModel):
    name: str
    producer_id: str
    description: Optional[str] = None
    specifications: Optional[Dict[str, Any]] = None

class CreateProduct(ProductBase):
    pass

class Product(ProductBase):
    id: str = Field(alias="_id") 

    class Config:
        from_attributes = True
