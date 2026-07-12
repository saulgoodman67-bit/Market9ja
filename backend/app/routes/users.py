from fastapi import APIRouter
from app.schemas.user import UserCreate

router = APIRouter(prefix="/users", tags=["Users"])

fake_db = []

@router.post("/register")
def register(user: UserCreate):
    fake_db.append(user.dict())

    return {
        "message": "User registered successfully",
        "email": user.email
    }
