from sqlalchemy import Column, Date, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models.base import Base


class Pesagem(Base):
    __tablename__ = 'pesagem'
    id = Column(Integer, primary_key=True, autoincrement=True)
    animal_id = Column(Integer, ForeignKey('animal.id'))
    peso = Column(Float)
    data = Column(Date)

    animal = relationship("Animal", back_populates="pesagem")
