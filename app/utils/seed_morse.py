from sqlalchemy.orm import Session
from code.models.dict import Dict, DicLine

MORSE_TABLE = [
    {"key": "A", "valeur": ".-"},
    {"key": "B", "valeur": "-..."},
    {"key": "C", "valeur": "-.-."},
    {"key": "D", "valeur": "-.."},
    {"key": "E", "valeur": "."},
    {"key": "F", "valeur": "..-."},
    {"key": "G", "valeur": "--."},
    {"key": "H", "valeur": "...."},
    {"key": "I", "valeur": ".."},
    {"key": "J", "valeur": ".---"},
    {"key": "K", "valeur": "-.-"},
    {"key": "L", "valeur": ".-.."},
    {"key": "M", "valeur": "--"},
    {"key": "N", "valeur": "-."},
    {"key": "O", "valeur": "---"},
    {"key": "P", "valeur": ".--."},
    {"key": "Q", "valeur": "--.-"},
    {"key": "R", "valeur": ".-."},
    {"key": "S", "valeur": "..."},
    {"key": "T", "valeur": "-"},
    {"key": "U", "valeur": "..-"},
    {"key": "V", "valeur": "...-"},
    {"key": "W", "valeur": ".--"},
    {"key": "X", "valeur": "-..-"},
    {"key": "Y", "valeur": "-.--"},
    {"key": "Z", "valeur": "--.."},
]

def seed_morse_dictionary(db: Session):

    existing = db.query(Dict).filter(Dict.name == "morse").first()

    if existing:
        print("Dictionnaire Morse déjà présent")
        return

    morse_dict = Dict(name="morse")
    db.add(morse_dict)
    db.commit()
    db.refresh(morse_dict)

    for entry in MORSE_TABLE:
        line = DicLine(
            Key=entry["key"],
            valeur=entry["valeur"],
            dictid=morse_dict.dictid
        )
        db.add(line)

    db.commit()
