"""Módulo de modelo de usuário."""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, relationship

from app.database import Base


class Usuario(Base):
    """Modelo de usuário."""
    __tablename__ = 'usuario'

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String)
    password = Column(String)
    pessoa_id = Column(Integer, ForeignKey('pessoa.id'))

    pessoa = relationship("Pessoa")
