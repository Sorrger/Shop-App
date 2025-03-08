from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.orm import relationship
from database.mongo import Base
from bson import ObjectId

class Product(Base):
    __tablename__ = "products"
    
    # SQLAlchemy fields
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    photo_url = Column(String, nullable=True)
    description = Column(Text, nullable=True)
    producer_id = Column(Integer, index=True)
    specifications = Column(Text, nullable=True) 

    producer = relationship("Producer", back_populates="products")

    mongo_id = Column(String, default=str(ObjectId()))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mongo_id = str(ObjectId()) 