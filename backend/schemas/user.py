from pydantic import BaseModel, validator
from datetime import datetime

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str
    role: str = "user"

    @validator('role')
    def validate_role(cls, value):
        if value not in ["user", "admin"]:
            raise ValueError('Role must be either "user" or "admin"')
        return value

class UserResponse(UserBase):
    id: int
    role: str
    created_at: datetime

    class Config:
        orm_mode = True
