from pydantic import BaseModel
from configurations.database_config import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    users = relationship("User", back_populates="role")


class RoleBase(BaseModel):
    name: str


class RoleDTO(BaseModel):
    id: int
    name: str

