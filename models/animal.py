from sqlalchemy import Column, Date, Enum, Float, Integer, String
from sqlalchemy.orm import Mapped, relationship

from models.base import Base


class Animal(Base):
    __tablename__ = 'animal'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
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
    peso_nascimento = Column(Float)

    pesagens = relationship("Pesagem", back_populates="animais")
