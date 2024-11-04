from datetime import datetime
from pydantic import BaseModel
from configurations.database_config import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from models.user import groupe_user_association


class Groupe(Base):
    __tablename__ = 'groupes'
    id = Column(Integer, primary_key=True, index=True)
    titre = Column(String(100), index=True)
    description = Column(String(255), index=True)
    createdDate = Column(DateTime, default=datetime.utcnow)
    updatedDate = Column(DateTime, default=datetime.utcnow)
    taches = relationship("Tache", back_populates="groupe")
    users = relationship("User", secondary=groupe_user_association, back_populates="groupes")


class GroupeBase(BaseModel):
    titre: str
    description: str


class GroupeDTO(BaseModel):
    id: int
    titre: str
    description: str
    createdDate: datetime
    updatedDate: datetime
