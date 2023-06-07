"""Modelo de animal."""

from sqlalchemy import Column, Date, Enum, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, relationship

from app.database import Base


class Animal(Base):
    """Modelo de animal."""
    __tablename__ = "animal"

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    chip: Mapped[str] = Column(String, nullable=True)
    brinco: Mapped[str] = Column(String, nullable=True)
    origem = Column(String, nullable=True)
    raca_id = Column(Integer, ForeignKey("raca.id"), nullable=True)
    id_mae = Column(Integer, nullable=True)
    id_pai = Column(Integer, nullable=True)
    sexo = Column(Enum("Macho", "Fêmea", name="sexo"), nullable=True)
    data_entrada = Column(Date, nullable=True)
    data_nascimento = Column(Date, nullable=True)
    peso = Column(Float, nullable=True)
    lote_id = Column(Integer, ForeignKey("lote.id"), nullable=True)

    lote_log = relationship("LoteLog", back_populates="animal")
    lote = relationship("Lote", back_populates="animais")
    peso_log = relationship("PesoLog", back_populates="animal")
    raca = relationship("Raca", back_populates="animais")
