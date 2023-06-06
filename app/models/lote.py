"""Modelo de lote."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, relationship

from app.database import Base


class Lote(Base):
    """Modelo de lote."""
    __tablename__ = "lote"

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    referencia = Column(String)
    numero = Column(Integer)
    descricao = Column(String)

    animais = relationship("Animal", back_populates="lote")
