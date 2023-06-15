from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, relationship

from app.models.base import Base


class Lote(Base):
    __tablename__ = "lote"

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = Column(String)
    numero: Mapped[int] = Column(Integer)
    dieta_id = Column(Integer, ForeignKey("dieta.id"), nullable=True)
    obs: Mapped[str] = Column(String, nullable=True)

    lote_log = relationship("LoteLog", back_populates="lote")
    animais = relationship("Animal", back_populates="lote")
    dieta = relationship("Dieta", back_populates="lote")
