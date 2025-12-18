from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from code.models.schemas.params import TradParams
from code.models.schemas.res import TradResponse
from code.handlers.trad import handle_translation
from code.middlewares.db import get_db

router = APIRouter(prefix="/trad", tags=["Traduction"])

@router.post("/", response_model=TradResponse)
def translate(params: TradParams, db: Session = Depends(get_db)):
    return handle_translation(db, params)
