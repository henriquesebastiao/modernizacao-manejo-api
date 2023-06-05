from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Pessoa(Base):
    __tablename__ = 'pessoa'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    sobre_nome = Column(String)
    cargo_id = Column(Integer, ForeignKey('cargo.id'))

    cargo = relationship("Cargo")
