from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class Cargo(Base):
    __tablename__ = 'cargo'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column(String(60), nullable=False)
