from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


from models.base import Base


class Fazenda(Base):
    __tablename__ = 'fazenda'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fazendeiro_id = Column(Integer, ForeignKey('fazendeiro.id'))
    nome = Column(String)

    fazendeiro = relationship("Fazendeiro")
