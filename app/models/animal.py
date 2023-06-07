"""Modelo de animal."""

from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, relationship

from app.models.base import Base


class Animal(Base):
    """Modelo de animal."""
    __tablename__ = "animal"

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    chip: Mapped[str] = Column(String)
    brinco: Mapped[str] = Column(String)
    origem = Column(String, nullable=True)
    raca_id = Column(Integer, ForeignKey("raca.id"), nullable=True)
    mae_id = Column(Integer, nullable=True)
    pai_id = Column(Integer, nullable=True)
    sexo: Mapped[str] = Column(String)
    data_entrada = Column(Date, nullable=True)
    data_nascimento = Column(Date, nullable=True)
    peso = Column(Float, nullable=True)
    lote_id = Column(Integer, ForeignKey("lote.id"), nullable=True)

    lote_log = relationship("LoteLog", back_populates="animal")
    lote = relationship("Lote", back_populates="animais")
    peso_log = relationship("PesoLog", back_populates="animal")
    raca = relationship("Raca", back_populates="animais")
