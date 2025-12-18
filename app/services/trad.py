from sqlalchemy.orm import Session
from code.models.trad import Trad
from code.models.dict import Dict, DicLine
from code.repositories.trad import save_trad

def translate_word(db: Session, word: str, dictionnary: str) -> Trad:
    letters = list(word)
    dico = db.query(Dict).filter(Dict.name == dictionnary).first()

    traduction = []
    for lettre in letters:
        line = db.query(DicLine).filter(
            DicLine.Key == lettre,
            DicLine.dictid == dico.dictid
        ).first()
        if line:
            traduction += line.valeur

    trad = "".join(traduction)

    trad_obj = Trad(word=word, trad=trad, dictionnary=dictionnary)
    return save_trad(db, trad_obj)
