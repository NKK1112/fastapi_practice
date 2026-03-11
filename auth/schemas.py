from pydantic import BaseModel, EmailStr

# Schema for new user craete
class UserCreate(BaseModel):
    username: str
    email:EmailStr
    password:str
    role:str

# Scheme for user login
class UserLogin(BaseModel):
    username:str
    password:str

