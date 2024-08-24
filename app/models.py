from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, registry

table_registry = registry()


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


@table_registry.mapped_as_dataclass
class Breed:
    __tablename__ = 'breed'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name: Mapped[str]


@table_registry.mapped_as_dataclass
class Employment:
    __tablename__ = 'employment'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    farmer_id: Mapped[int] = mapped_column(ForeignKey('farmer.id'))
    farm_id: Mapped[int] = mapped_column(ForeignKey('farm.id'))
    employment_position_id: Mapped[int] = mapped_column(
        ForeignKey('employment_position.id')
    )


@table_registry.mapped_as_dataclass
class EmploymentPosition:
    __tablename__ = 'employment_position'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name: Mapped[str]


@table_registry.mapped_as_dataclass
class Farm:
    __tablename__ = 'farm'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name: Mapped[str]


@table_registry.mapped_as_dataclass
class Farmer:
    __tablename__ = 'farmer'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    farmer_plan_id: Mapped[int] = mapped_column(ForeignKey('farmer_plan.id'))


@table_registry.mapped_as_dataclass
class FarmerPlan:
    __tablename__ = 'farmer_plan'
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    plan: Mapped[str]


@table_registry.mapped_as_dataclass
class User:
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    first_name: Mapped[str]
    last_name: Mapped[str | None]
    phone: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]
    create_at: Mapped[datetime] = mapped_column(default=datetime.now())
    update_at: Mapped[datetime] = mapped_column(
        default=datetime.now(), onupdate=datetime.now()
    )
    active: Mapped[bool] = mapped_column(default=True)

    user_type_id: Mapped[int] = mapped_column(
        ForeignKey('user_type.id'), default=1
    )
    manager_id: Mapped[int | None] = mapped_column(
        ForeignKey('user.id'), nullable=True, default=1
    )


@table_registry.mapped_as_dataclass
class UserType:
    __tablename__ = 'user_type'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    type: Mapped[str]
