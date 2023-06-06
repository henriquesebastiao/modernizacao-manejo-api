"""Modelo de lote log log."""

from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.orm import Mapped, relationship

from app.database import Base


class LoteLog(Base):
    """Modelo de lote log."""
    __tablename__ = "lote_log"

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    data_entrada = Column(Date)
    data_saida = Column(Date)
    animal_id = Column(Integer, ForeignKey("animal.id"))
    lote_id = Column(Integer, ForeignKey("lote.id"))

    animal = relationship("Animal", back_populates="lote_log")
    lote = relationship("Lote", back_populates="lote_log")
