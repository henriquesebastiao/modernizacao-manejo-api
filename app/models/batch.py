from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import table_registry


@table_registry.mapped_as_dataclass
class Batch:
    __tablename__ = 'batch'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    reg: Mapped[str] = mapped_column(nullable=False)
    farm_id: Mapped[int] = mapped_column(ForeignKey('farm.id'))


@table_registry.mapped_as_dataclass
class BatchLog:
    __tablename__ = 'batch_log'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    batch_id: Mapped[int] = mapped_column(ForeignKey('batch.id'))
    animal_id: Mapped[int] = mapped_column(ForeignKey('animal.id'))
    entry_date: Mapped[datetime]
    departure_date: Mapped[datetime]
