"""Módulo de modelo de pessoa."""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, relationship

from app.database import Base


class Pessoa(Base):
    """Modelo de pessoa."""
    __tablename__ = 'pessoa'

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    sobre_nome: Mapped[str] = Column(String)
    cargo_id = Column(Integer, ForeignKey('cargo.id'))

    cargo = relationship("Cargo")
