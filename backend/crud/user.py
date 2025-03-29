from sqlalchemy.orm import Session
from argon2 import PasswordHasher
from models.user import User
from schemas.user import UserCreate

ph = PasswordHasher()
# === CREATE ===

def createUser(db: Session, user: UserCreate):
    hashed_password = ph.hash(user.password)
    new_user = User(email=user.email, password_hash=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
# === READ ===
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()
# === UPDATE ===
# === DELETE ===