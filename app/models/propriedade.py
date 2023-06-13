from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped

from app.models.base import Base


class Propriedade(Base):
    __tablename__ = 'propriedade'

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = Column(String)
    fazendeiro_id = Column(Integer)
