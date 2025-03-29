from pydantic import BaseModel

class ProducerBase(BaseModel):
    name: str

class CreateProducer(ProducerBase):
    pass

class Producer(ProducerBase):
    id: int

    class Config:
        orm_mode = True
