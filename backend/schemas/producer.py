from pydantic import BaseModel
from typing import Optional

class ProducerBase(BaseModel):
    name: str
    country: Optional[str] = None

class CreateProducer(ProducerBase):
    pass

class Producer(ProducerBase):
    id: int

    class Config:
        orm_mode = True
