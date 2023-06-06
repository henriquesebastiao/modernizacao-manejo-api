"""Modelo de animal."""

from sqlalchemy import Column, Date, Enum, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, relationship

from app.database import Base


class Animal(Base):
    """Modelo de animal."""
    __tablename__ = "animal"

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    chip = Column(String)
    brinco = Column(String)
    origem = Column(String)
    raca_id = Column(Integer, ForeignKey("racas.id"))  # Verificar o que associar aqui, se é o id da raça ou o nome
    id_mae = Column(Integer)
    id_pai = Column(Integer)
    sexo = Column(Enum("Macho", "Fêmea", name="sexo"))
    data_entrada = Column(Date)
    data_nascimento = Column(Date)
    peso = Column(Float)
    lote_id = Column(Integer, ForeignKey("lote.id"))

    lote_log = relationship("LoteLog", back_populates="animal")
    lote = relationship("Lote", back_populates="animais")
    peso_log = relationship("PesoLog", back_populates="animal")
    raca = relationship("Raca", back_populates="animais")
