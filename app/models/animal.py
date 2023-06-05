"""Modelo de animal."""

from sqlalchemy import Column, Date, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, relationship

from app.database import Base


class Animal(Base):
    """Modelo de animal."""
    __tablename__ = 'animal'

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    chip = Column(Integer)
    brinco = Column(Integer)
    origem = Column(String)
    raca = Column(Enum(
        'Nelore',
        'Angus',
        'Guzerá',
        'Senepol',
        'Outra',
        name='raca'
    ))
    id_mae = Column(Integer)
    id_pai = Column(Integer)
    sexo = Column(Enum('Macho', 'Fêmea', name='sexo'))
    data_entrada = Column(Date)
    data_nascimento = Column(Date)
    pesagem_id = Column(Integer, ForeignKey('pesagem.id'))

    pesagens = relationship("Pesagem", back_populates="animais")
