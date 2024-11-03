from datetime import datetime

from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, DateTime, Boolean

from configurations.database_config import Base


class Tache(Base):
    __tablename__ = 'taches'
    id = Column(Integer, primary_key=True, index=True)
    titre = Column(String(100))
    date_echeance = Column(DateTime, default=datetime.utcnow)
    fait = Column(Boolean, default=False)


class TacheBase(BaseModel):
    titre: str
    date_echeance: datetime


class TacheDTO(BaseModel):
    id: int
    titre: str
    date_echeance: datetime
    fait: bool
