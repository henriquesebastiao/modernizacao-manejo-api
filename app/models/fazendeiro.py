"""Módulo do modelo de fazendeiro."""

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import Mapped, relationship

from app.models.base import Base


class Fazendeiro(Base):
    """Modelo de fazendeiro."""
    __tablename__ = 'fazendeiro'

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))

    fazenda = relationship("Fazenda", back_populates="fazendeiro")
