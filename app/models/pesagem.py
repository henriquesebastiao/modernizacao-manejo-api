"""Módulo de modelo de pesagem."""

from sqlalchemy import Column, Date, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.database import Base


class Pesagem(Base):
    """Modelo de pesagem."""
    __tablename__ = "pesagem"

    id = Column(Integer, primary_key=True)
    animal_id = Column(Integer, ForeignKey("animal.id"))
    data = Column(Date)
    peso = Column(Float)

    animal = relationship("Animal", back_populates="pesagens")
