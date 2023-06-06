"""Modelo de raça."""

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Mapped, relationship

from app.database import Base


class Raca(Base):
    """Modelo de raça."""
    __tablename__ = "racas"

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, unique=True)

    animais = relationship("Animal", back_populates="raca")
