from fastapi import APIRouter
from sqlalchemy.testing import db

import app.schemas
import app.models
from sqlalchemy.orm import Session

from app import schemas, models, database

router = APIRouter(
    prefix='/card',
    tags=['Card']
)
@router.post('/')
def card_create(card: schemas.Card):
    hashed_cvv = hash(card.code)
    card.cvv = hashed_cvv


    new_user = models.Card(**card.dict())
    db.add(card_create)
    db.commit()

    return card_create
