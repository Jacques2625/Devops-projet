from pydantic import BaseModel

class IndexResponse(BaseModel):
    msg: str

class TradResponse(BaseModel):
    word: str
    dictionnary: str
    trad: str
