from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from models.base import Base


class Pessoa(Base):
    __tablename__ = 'pessoa'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    sobre_nome = Column(String)
    cargo_id = Column(Integer, ForeignKey('cargo.id'))

    cargo = relationship("Cargo")
