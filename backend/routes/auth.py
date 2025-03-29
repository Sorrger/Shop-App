from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.user import UserCreate
from argon2 import PasswordHasher
import jwt
import datetime
import os
from fastapi.security import OAuth2PasswordBearer
from argon2.exceptions import VerifyMismatchError
from database.mysql import SessionLocal
from crud.user import create_user, get_user_by_email
from schemas.user import UserCreate, UserResponse
from database.mysql import get_db


router = APIRouter()
ph = PasswordHasher()
SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    return create_user(db, user)

@router.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    try:
        ph.verify(db_user.password_hash, user.password)
    except VerifyMismatchError:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    token_payload = {
        "sub": db_user.email,
        "role": db_user.role,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    token = jwt.encode(token_payload, SECRET_KEY, algorithm="HS256")

    return {"access_token": token, "token_type": "bearer"}