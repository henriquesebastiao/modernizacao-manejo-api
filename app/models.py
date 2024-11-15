from datetime import datetime
from enum import Enum
from zoneinfo import ZoneInfo

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, registry

table_registry = registry()


class Breed(str, Enum):
    girolando = 'girolando'
    guzera = 'guzera'
    holandes = 'holandes'
    nelore = 'nelore'
    senepol = 'senepol'
    gir_leiteiro = 'gir_leiteiro'
    tabapua = 'tabapua'
    angus = 'angus'
    brahman = 'brahman'
    sindi = 'sindi'


@table_registry.mapped_as_dataclass
class Animal:
    __tablename__ = 'animal'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    tag: Mapped[int]
    gender: Mapped[str]
    origin: Mapped[str]
    sisbov: Mapped[int | None] = mapped_column(default=None)
    breed: Mapped[Breed] = mapped_column(default=Breed.nelore)
    father_id: Mapped[int | None] = mapped_column(default=None)
    mother_id: Mapped[int | None] = mapped_column(default=None)
    birth_date: Mapped[datetime | None] = mapped_column(default=None)
    buy_date: Mapped[datetime | None] = mapped_column(default=None)
    sell_date: Mapped[datetime | None] = mapped_column(default=None)


@table_registry.mapped_as_dataclass
class AnimalWeight:
    __tablename__ = 'animal_weight'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    weight_type: Mapped[str]
    animal_tag: Mapped[int]
    weight: Mapped[float]
    weight_date: Mapped[datetime]


@table_registry.mapped_as_dataclass
class Batch:
    __tablename__ = 'batch'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    reg: Mapped[str] = mapped_column(nullable=False)
    farm_id: Mapped[int] = mapped_column(ForeignKey('farm.id'))


@table_registry.mapped_as_dataclass
class BatchLog:
    __tablename__ = 'batch_log'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    batch_id: Mapped[int] = mapped_column(ForeignKey('batch.id'))
    animal_id: Mapped[int] = mapped_column(ForeignKey('animal.id'))
    entry_date: Mapped[datetime]
    departure_date: Mapped[datetime]


class EmploymentPosition(str, Enum):
    farmer = 'farmer'
    manager = 'manager'
    cowboy = 'cowboy'


@table_registry.mapped_as_dataclass
class Employment:
    __tablename__ = 'employment'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    farmer_id: Mapped[int] = mapped_column(ForeignKey('farmer.id'))
    farm_id: Mapped[int] = mapped_column(ForeignKey('farm.id'))
    employment_position: Mapped[EmploymentPosition]


@table_registry.mapped_as_dataclass
class Farm:
    __tablename__ = 'farm'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str]


class FarmerPlan(str, Enum):
    free = 'free'
    starter = 'starter'
    pro = 'pro'


@table_registry.mapped_as_dataclass
class Farmer:
    __tablename__ = 'farmer'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), unique=True)
    farmer_plan: Mapped[FarmerPlan] = mapped_column(default='free')


@table_registry.mapped_as_dataclass
class User:
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    first_name: Mapped[str | None] = mapped_column(default=None)
    last_name: Mapped[str | None] = mapped_column(default=None)
    phone: Mapped[str | None] = mapped_column(default=None)
    create_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now(), nullable=False
    )
    update_at: Mapped[datetime] = mapped_column(
        init=False,
        server_default=func.now(),
        onupdate=datetime.now(tz=ZoneInfo('UTC')),
        nullable=False,
    )
    active: Mapped[bool] = mapped_column(default=True)
    manager_id: Mapped[int | None] = mapped_column(
        ForeignKey('user.id'), default=None
    )
