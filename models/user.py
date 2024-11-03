from configurations.database_config import DataBase
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from models.role import RoleDTO


class User(DataBase):
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
