from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import table_registry


@table_registry.mapped_as_dataclass
class Animal:
    __tablename__ = 'animal'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    tag: Mapped[int]
    sisbov: Mapped[int]
    gender: Mapped[str]
    breed_id: Mapped[int]
    father_id: Mapped[int]
    mother_id: Mapped[int]
    origin_id: Mapped[int]
    birth_date: Mapped[datetime]
    buy_date: Mapped[datetime]
    sell_date: Mapped[datetime]


@table_registry.mapped_as_dataclass
class AnimalWeightType:
    __tablename__ = 'animal_weight_type'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name: Mapped[str]


@table_registry.mapped_as_dataclass
class AnimalWeight:
    __tablename__ = 'animal_weight'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    weight_type_id: Mapped[int]
    animal_id: Mapped[int]
    weight: Mapped[float]
    weight_date: Mapped[datetime]
