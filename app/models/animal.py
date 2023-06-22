from datetime import date

from sqlalchemy import Date, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class Animal(Base):
    __tablename__ = 'animal'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    tag: Mapped[int] = mapped_column(Integer, nullable=True)
    sisbov: Mapped[int] = mapped_column(Integer, nullable=True)
    gender: Mapped[str] = mapped_column(String, nullable=True)
    breed_id: Mapped[int] = mapped_column(Integer, nullable=True)
    father_id: Mapped[int] = mapped_column(Integer, nullable=True)
    mother_id: Mapped[int] = mapped_column(Integer, nullable=True)
    origin_id: Mapped[int] = mapped_column(Integer, nullable=True)
    birth_date: Mapped[date] = mapped_column(Date, nullable=True)
    buy_date: Mapped[date] = mapped_column(Date, nullable=True)
    sell_date: Mapped[date] = mapped_column(Date, nullable=True)
