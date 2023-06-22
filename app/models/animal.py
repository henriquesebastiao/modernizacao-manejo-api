from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class Animal(Base):
    __tablename__ = 'animal'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    tag: Mapped[str] = mapped_column(Integer, nullable=False)
    sisbov: Mapped[str] = mapped_column(Integer, nullable=False)
    gender: Mapped[str] = mapped_column(Integer, nullable=False)
    breed_id: Mapped[int] = mapped_column(Integer, nullable=False)
    father_id: Mapped[int] = mapped_column(Integer, nullable=False)
    mother_id: Mapped[int] = mapped_column(Integer, nullable=False)
    origin_id: Mapped[str] = mapped_column(Integer, nullable=False)
    birth_date: Mapped[str] = mapped_column(Integer, nullable=False)
    buy_date: Mapped[str] = mapped_column(Integer, nullable=False)
    sell_date: Mapped[str] = mapped_column(Integer, nullable=False)
