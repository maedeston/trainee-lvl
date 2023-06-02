from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional



class UserBase(BaseModel):
    id: int
    email: EmailStr
    password: str

class UserOut(BaseModel):
    email: str

    class Config:
        orm_mode = True

class UserCreate(UserBase):
    pass