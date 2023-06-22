from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class BatchLog(Base):
    __tablename__ = "batch_log"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    batch_id: Mapped[int] = mapped_column(Integer, ForeignKey('batch.id'))
    animal_id: Mapped[int] = mapped_column(Integer, ForeignKey('animal.id'))
    entry_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    departure_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)
