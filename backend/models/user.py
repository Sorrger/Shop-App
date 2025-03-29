from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from database.mysql import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(50), default="user") 
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())