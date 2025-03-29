from fastapi import APIRouter, Depends
from dependencies.auth import require_role

router = APIRouter()

@router.get("/dashboard")
def admin_dashboard(user=Depends(require_role("admin"))):
    return {"message": "Welcome to the Admin Dashboard!", "user": user}
