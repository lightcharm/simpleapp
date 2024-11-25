from fastapi import APIRouter, HTTPException
from app.models import User
from app.storage import storage

router = APIRouter()

# Get all users
@router.get("/")
async def get_users():
    return storage

# Get an user
@router.get("/{email}")
async def get_user(email: str):
    user = storage.get(email)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"email": email, "full_name": user["full_name"]}

# Create an user
@router.post("/")
async def create_user(user: User):
    if user.email in storage:
        raise HTTPException(status_code=400, detail="User already exists")
    
    storage[user.email] = {"full_name": user.full_name}
    return {"message": "User created", "user": user.dict()}
