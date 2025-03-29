import jwt
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        if "role" not in payload:
            raise HTTPException(status_code=401, detail="Role missing in token")
        return {"email": payload["sub"], "role": payload["role"]}
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")


def require_role(required_role: str):
    def role_dependency(user: dict = Depends(get_current_user)):
        if user["role"] != required_role:
            raise HTTPException(status_code=403, detail=f"Access denied: {required_role} role required")
        return user
    return role_dependency
