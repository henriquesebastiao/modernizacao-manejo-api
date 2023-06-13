from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped

from app.models.base import Base


class Cargo(Base):
    __tablename__ = 'cargo'

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = Column(String)
