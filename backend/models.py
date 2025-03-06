from sqlalchemy import Column, ForeignKey, Integer, String, Numeric
from sqlalchemy.orm import relationship
from database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    photo_url = Column(String)
    description = Column(String, index=True)
    price = Column(Numeric(10, 2))
    producer_id = Column(Integer, ForeignKey('producers.id'))

    producer = relationship("Producer", back_populates="products")

class Producer(Base):
    __tablename__ = "producers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    products = relationship("Product", back_populates="producer")

    