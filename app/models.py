from datetime import date, datetime
from typing import List, Optional
from zoneinfo import ZoneInfo

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, registry, relationship

from app.utils.enum import (
    Breeds,
    EmploymentPositions,
    FarmerPlan,
    Genders,
    WeightTypes,
)

# Read more about the SQLAlchemy concepts used here:
# https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html
# https://docs.sqlalchemy.org/en/20/orm/relationship_api.html
# https://docs.sqlalchemy.org/en/20/orm/self_referential.html
# About dataclass errors: https://docs.sqlalchemy.org/en/20/errors.html#error-dcte

table_registry = registry()


@table_registry.mapped_as_dataclass
class User:
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    first_name: Mapped[str]
    last_name: Mapped[Optional[str]] = mapped_column(default=None)
    phone: Mapped[Optional[str]] = mapped_column(default=None)
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        init=False,
        server_default=func.now(),
        onupdate=datetime.now(tz=ZoneInfo('UTC')),
    )
    active: Mapped[Optional[bool]] = mapped_column(default=True)
    manager_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey('users.id'), default=None
    )

    manager: Mapped['User'] = relationship(
        remote_side=[id], init=False, foreign_keys='User.manager_id'
    )
    farmer: Mapped['Farmer'] = relationship(
        back_populates='user', lazy='immediate', init=False
    )
    employment: Mapped['Employment'] = relationship(
        back_populates='user', lazy='immediate', init=False
    )


@table_registry.mapped_as_dataclass
class Farmer:
    __tablename__ = 'farmers'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), unique=True)
    farmer_plan: Mapped[FarmerPlan] = mapped_column(default=FarmerPlan.FREE)

    user: Mapped['User'] = relationship(
        back_populates='farmer', lazy='immediate', init=False
    )
    employment: Mapped[List['Employment']] = relationship(
        back_populates='farmer', lazy='immediate', init=False
    )


@table_registry.mapped_as_dataclass
class Farm:
    __tablename__ = 'farms'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str]

    employment: Mapped[List['Employment']] = relationship(
        back_populates='farm', lazy='immediate', init=False
    )
    batch: Mapped[List['Batch']] = relationship(
        back_populates='farm', lazy='immediate', init=False
    )


@table_registry.mapped_as_dataclass
class Employment:
    __tablename__ = 'employments'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    farmer_id: Mapped[int] = mapped_column(ForeignKey('farmers.id'))
    farm_id: Mapped[int] = mapped_column(ForeignKey('farms.id'))
    employment_position: Mapped[EmploymentPositions]

    user: Mapped['User'] = relationship(
        back_populates='employment', lazy='immediate', init=False
    )
    farmer: Mapped['Farmer'] = relationship(
        back_populates='employment', lazy='immediate', init=False
    )
    farm: Mapped['Farm'] = relationship(
        back_populates='employment', lazy='immediate', init=False
    )


@table_registry.mapped_as_dataclass
class Batch:
    __tablename__ = 'batchs'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    farm_id: Mapped[int] = mapped_column(ForeignKey('farms.id'))
    description: Mapped[Optional[str]]

    farm: Mapped['Farm'] = relationship(
        back_populates='batch', lazy='immediate', init=False
    )
    batch_log: Mapped[List['BatchLog']] = relationship(
        back_populates='batch', lazy='immediate', init=False
    )


@table_registry.mapped_as_dataclass
class Animal:
    __tablename__ = 'animals'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    tag: Mapped[int]
    gender: Mapped[Genders]
    origin: Mapped[Optional[str]] = mapped_column(default=None)
    sisbov: Mapped[Optional[int]] = mapped_column(default=None)
    breed: Mapped[Breeds] = mapped_column(default=Breeds.NELORE)
    father_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey('animals.id'), default=None
    )
    mother_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey('animals.id'), default=None
    )
    birth_date: Mapped[Optional[date]] = mapped_column(default=None)
    buy_date: Mapped[Optional[date]] = mapped_column(default=None)
    sell_date: Mapped[Optional[date]] = mapped_column(default=None)
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        init=False,
        server_default=func.now(),
        onupdate=datetime.now(tz=ZoneInfo('UTC')),
    )

    father: Mapped['Animal'] = relationship(
        remote_side=[id], init=False, foreign_keys='Animal.father_id'
    )
    mother: Mapped['Animal'] = relationship(
        remote_side=[id], init=False, foreign_keys='Animal.mother_id'
    )
    animal_weight: Mapped[List['AnimalWeight']] = relationship(
        back_populates='animal', lazy='immediate', init=False
    )
    batch_log: Mapped[List['BatchLog']] = relationship(
        back_populates='animal', lazy='immediate', init=False
    )


@table_registry.mapped_as_dataclass
class AnimalWeight:
    __tablename__ = 'animal_weights'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    weight_type: Mapped[WeightTypes]
    animal_id: Mapped[int] = mapped_column(ForeignKey('animals.id'))
    weight: Mapped[float]
    weight_date: Mapped[date]

    animal: Mapped['Animal'] = relationship(
        back_populates='animal_weight', lazy='immediate', init=False
    )


@table_registry.mapped_as_dataclass
class BatchLog:
    __tablename__ = 'batch_logs'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    batch_id: Mapped[int] = mapped_column(ForeignKey('batchs.id'))
    animal_id: Mapped[int] = mapped_column(ForeignKey('animals.id'))
    entry_date: Mapped[datetime]
    departure_date: Mapped[datetime]

    batch: Mapped['Batch'] = relationship(
        back_populates='batch_log', lazy='immediate', init=False
    )
    animal: Mapped['Animal'] = relationship(
        back_populates='batch_log', lazy='immediate', init=False
    )
