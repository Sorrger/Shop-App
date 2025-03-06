from typing import Optional
from pydantic import BaseModel

class CreateProduct(BaseModel):
    name: str
    photo_url: Optional[str] = None
    description: Optional[str] = None
    price: float
    producer_id: int

    class Config:
        orm_mode = True

class CreateProducer(BaseModel):
    name: str

    class Config:
        orm_mode = True