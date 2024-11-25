from fastapi import FastAPI
from app.routers import users

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["Users"])

@app.get("/")
async def root():
    return {"message": "Welcome to app"}
