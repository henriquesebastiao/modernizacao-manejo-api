from sqlalchemy import Column, Date, Float, Integer, String, Enum
from sqlalchemy.orm import relationship, validates

from models.base import Base


class Animal(Base):
    __tablename__ = 'animal'

    id = Column(Integer, primary_key=True, autoincrement=True)
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
