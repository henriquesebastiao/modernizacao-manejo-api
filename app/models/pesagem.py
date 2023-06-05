"""Módulo de modelo de pesagem."""

from sqlalchemy import Column, Date, Float, ForeignKey, Integer
from sqlalchemy.orm import Mapped, relationship

from app.database import Base


class Pesagem(Base):
    """Modelo de pesagem."""
    __tablename__ = 'pesagem'

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    id_animal = Column(Integer, ForeignKey('animal.id'))
    peso = Column(Float)
    data = Column(Date)

    animais = relationship("Animal", back_populates="pesagens")
