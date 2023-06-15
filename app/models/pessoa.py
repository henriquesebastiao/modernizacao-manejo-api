from datetime import date

from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import Mapped, relationship

from app.models.base import Base


class Pessoa(Base):
    __tablename__ = 'pessoa'

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    cpf: Mapped[str] = Column(String, unique=True)
    data_nascimento: Mapped[date] = Column(Date, nullable=True)
    nome = Column(String)
    sobrenome: Mapped[str] = Column(String, nullable=True)
    cargo_id = Column(Integer, ForeignKey('cargo.id'))

    cargo = relationship("Cargo")
