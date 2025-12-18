from sqlalchemy.orm import Session
from code.models.trad import Trad

def save_trad(db: Session, trad: Trad):
    db.add(trad)
    db.commit()
    db.refresh(trad)
    return trad

def get_trad_by_word(db: Session, word: str):
    return db.query(Trad).filter(Trad.word == word).first()
