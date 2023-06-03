from sqlalchemy import Column, Date, Float, Integer, String, Enum

from models.base import Base


class Animal(Base):
    __tablename__ = 'animal'
    id = Column(Integer, primary_key=True, autoincrement=True)
    origem = Column(String)
    id_mae = Column(Integer)
    id_pai = Column(Integer)
    idade = Column(Integer)
    sexo = Column(Enum('Macho', 'Fêmea', name='sexo'))
    data_entrada = Column(Date)
    peso_nascimento = Column(Float)
