from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, relationship

from app.models.base import Base


class Dieta(Base):
    __tablename__ = "dieta"

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = Column(String)
    desc: Mapped[str] = Column(String, nullable=True)

    lote = relationship("Lote", back_populates="dieta")
