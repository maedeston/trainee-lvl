from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
import app.models

class Transaction(BaseModel):
    AFrom: int
    Ato: int
    count: int

class User(BaseModel):
    user_id: int
    email: str
    password: int

class Bank_Client(BaseModel):
    bank_client_id: int
    tax_id: int


