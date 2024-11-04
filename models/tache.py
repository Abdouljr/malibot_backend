from datetime import datetime

from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from configurations.database_config import Base
from models.groupe import GroupeDTO


class Tache(Base):
    __tablename__ = 'taches'
    id = Column(Integer, primary_key=True, index=True)
    titre = Column(String(100))
    date_echeance = Column(DateTime, default=datetime.utcnow)
    fait = Column(Boolean, default=False)
    groupe_id = Column(Integer, ForeignKey("groupes.id"))
    groupe = relationship("Groupe", back_populates="taches")


class TacheBase(BaseModel):
    titre: str
    date_echeance: datetime
    groupe_id: int


class TacheDTO(BaseModel):
    id: int
    titre: str
    date_echeance: datetime
    fait: bool
    groupe: GroupeDTO
