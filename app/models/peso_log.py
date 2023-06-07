"""Módulo de modelo de peso log."""

from sqlalchemy import Column, Date, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.models.base import Base

class PesoLog(Base):
    """Modelo de pesagem."""
    __tablename__ = "peso_log"

    id = Column(Integer, primary_key=True)
    animal_id = Column(Integer, ForeignKey("animal.id"))
    data = Column(Date)
    peso = Column(Float)

    animal = relationship("Animal", back_populates="peso_log")
