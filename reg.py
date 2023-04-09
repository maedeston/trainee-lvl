from fastapi import APIRouter
from sqlalchemy.testing import db

import app.schemas
import app.models
from sqlalchemy.orm import Session

from app import schemas, models, database

router = APIRouter(
    prefix='/user',
    tags=['Users']
)
@router.post('/')
def create_user(user: schemas.User):
    hashed_password = hash(user.password)
    user_password = hashed_password

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()

    return new_user
