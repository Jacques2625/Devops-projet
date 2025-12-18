from sqlalchemy.orm import Session
from code.models.schemas.params import TradParams
from code.services.trad import translate_word

def handle_translation(db: Session, params: TradParams):
    return translate_word(db, params.word, params.dictionnary)
