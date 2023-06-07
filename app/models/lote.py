"""Modelo de lote."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, relationship

from app.models.base import Base


class Lote(Base):
    """Modelo de lote."""
    __tablename__ = "lote"

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = Column(String)
    numero: Mapped[int] = Column(Integer)
    obs: Mapped[str] = Column(String)

    lote_log = relationship("LoteLog", back_populates="lote")
    animais = relationship("Animal", back_populates="lote")
