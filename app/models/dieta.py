"""Modelo de dieta."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, relationship

from app.models.base import Base


class Dieta(Base):
    """Modelo de dieta."""
    __tablename__ = "dieta"

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = Column(String)
    descricao: Mapped[str] = Column(String)

    lote = relationship("Lote", back_populates="dieta")
