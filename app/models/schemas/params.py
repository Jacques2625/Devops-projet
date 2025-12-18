from pydantic import BaseModel, Field

class Encodage(BaseModel):
    key: str
    valeur: str

class TradParams(BaseModel):
    word: str
    dictionnary: str = Field(
        default="morse",
        description="Dictionnaire de traduction (morse par défaut)"
    )

class CreateDict(BaseModel):
    dictionnary: str
    table: list[Encodage]

class DeleteDict(BaseModel):
    dictionnary: str
