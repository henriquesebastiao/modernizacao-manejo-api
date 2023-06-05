"""Módulo de modelo de fazenda."""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, relationship

from app.database import Base


class Fazenda(Base):
    """Modelo de fazenda."""
    __tablename__ = 'fazenda'

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    fazendeiro_id = Column(Integer, ForeignKey('fazendeiro.id'))
    nome = Column(String)

    fazendeiro = relationship("Fazendeiro", back_populates="fazendas")
