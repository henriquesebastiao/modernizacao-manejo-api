from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Mapped, relationship

from app.models.base import Base


class Raca(Base):
    __tablename__ = "raca"

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = Column(String, unique=True)

    animais = relationship("Animal", back_populates="raca")
