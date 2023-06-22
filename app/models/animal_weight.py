from datetime import datetime

from sqlalchemy import DateTime, Float, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class AnimalWeight(Base):
    __tablename__ = 'animal_weight'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    weight_type_id: Mapped[int] = mapped_column(Integer, nullable=False)
    animal_id: Mapped[int] = mapped_column(Integer, nullable=False)
    weight: Mapped[float] = mapped_column(Float, nullable=False)
    weight_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
