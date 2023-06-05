from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Fazenda(Base):
    __tablename__ = 'fazenda'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fazendeiro_id = Column(Integer, ForeignKey('fazendeiro.id'))
    nome = Column(String)

    fazendeiro = relationship("Fazendeiro", back_populates="fazendas")
