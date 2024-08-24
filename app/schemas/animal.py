from datetime import date, datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict


class Sexo(str, Enum):
    M = 'M'
    F = 'F'


class AnimalBase(BaseModel):
    tag: int | None
    sisbov: int | None
    gender: Sexo | None
    birth_date: date | None
    buy_date: date | None
    sell_date: date | None


class AnimalCreate(AnimalBase):
    breed: str | None
    father_tag: int | None
    mother_tag: int | None
    origin: str | None


class AnimalUpdate(AnimalBase):
    pass


class AnimalSchema(AnimalBase):
    model_config = ConfigDict(from_attributes=True)
    breed_id: int | None
    father_id: int | None
    mother_id: int | None
    origin_id: int | None


class AnimalWeightSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int | None
    weight_type_id: int | None
    animal_id: int | None
    weight: float | None
    weight_date: datetime | None


class AnimalWeightTypeSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int | None
    type: str | None
