from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from code.databases.mysql_session import Base

class Dict(Base):
    __tablename__ = "dict"

    dictid = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(60))

    dictionnary = relationship("DicLine", backref="dict")

class DicLine(Base):
    __tablename__ = "dicline"

    id = Column(Integer, primary_key=True, index=True)
    Key = Column(String(40))
    valeur = Column(String(40))
    dictid = Column(Integer, ForeignKey("dict.dictid"))
