from fastapi import APIRouter,  Depends

from sqlalchemy.orm import Session
from app import models, schemas, utils, database

router = APIRouter(
    tags=['Authentication']
)

@router.post('/login', response_model=schemas.Token)
def login(user: schemas.UserCreate, db: Session = Depends(database.get_db())):
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user





