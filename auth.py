from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session
from .. import models, schemas, utils, database, oauth2

router = APIRouter(
    tags=['Authentication']
)


@router.post('/login', response_model=schemas.Token)
def login(user_crecredentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db())):
    user = db.query(models.User).filter(
        models.User.email == user_crecredentials.username).first()

    if not user:
        raise HTTPException(
            )