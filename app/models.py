from pydantic import BaseModel, EmailStr

class User(BaseModel):
    email: EmailStr
    full_name: str
