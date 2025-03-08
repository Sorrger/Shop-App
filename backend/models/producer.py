from sqlalchemy import Column, Integer, String
from database.mysql import Base

class Producer(Base):
    __tablename__ = "producers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    country = Column(String, nullable=True)
