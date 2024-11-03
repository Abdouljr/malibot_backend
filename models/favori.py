from configurations.database_config import Base
from sqlalchemy import Column, Integer, String


class Favori(Base):
    __tablename__ = 'favoris'
    id = Column(Integer, primary_key=True, index=True)
    id_tache = Column(Integer)
    unique_id_user = Column(String(100))
