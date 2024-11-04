from configurations.database_config import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from models.role import RoleDTO


groupe_user_association = Table(
    'groupe_user',
    Base.metadata,
    Column('groupe_id', Integer, ForeignKey('groupes.id'), primary_key=True),
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True)
)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    unique_id = Column(String(100))
    email = Column(String(150))
    createdDate = Column(DateTime, default=datetime.utcnow)
    updatedDate = Column(DateTime, default=datetime.utcnow)
    username = Column(String(50))
    password = Column(String(255))
    profil = Column(String(255), default='')
    role_id = Column(Integer, ForeignKey("roles.id"))
    role = relationship("Role", back_populates="users")

    groupes = relationship("Groupe", secondary=groupe_user_association, back_populates="users")


# model d'entre
class UserBase(BaseModel):
    email: str
    password: str
    username: str
    profil: Optional[str] = ""


# model de sortie
class UserDTO(BaseModel):
    id: int
    unique_id: str
    email: str
    username: str
    profil: str
    role: RoleDTO
