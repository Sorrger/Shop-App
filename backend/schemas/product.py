from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

class ProductBase(BaseModel):
    name: str
    photo_url: Optional[str] = None
    description: Optional[str] = None
    producer_id: str
    specifications: Optional[Dict[str, Any]] = None


class CreateProduct(ProductBase):
    pass

class Product(ProductBase):
    id: str = Field(alias="_id")

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
