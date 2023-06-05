from sqlalchemy import Column, Date, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.database import Base


class Pesagem(Base):
    __tablename__ = 'pesagem'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_animal = Column(Integer, ForeignKey('animal.id'))
    peso = Column(Float)
    data = Column(Date)

    animais = relationship("Animal", back_populates="pesagens")
