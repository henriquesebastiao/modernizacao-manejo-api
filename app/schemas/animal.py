from datetime import date, datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict


class Sexo(str, Enum):
    M = 'M'
    F = 'F'


class AnimalBase(BaseModel):
    tag: int | None
    sisbov: int | None = None
    gender: Sexo | None
    birth_date: date | None = None
    buy_date: date | None = None


class AnimalCreate(AnimalBase):
    breed_id: int | None
    father_id: int | None = None
    mother_id: int | None = None
    origin: str | None


class AnimalUpdate(BaseModel):
    tag: int | None = None
    sisbov: int | None = None
    breed_id: int | None = None
    father_id: int | None = None
    mother_id: int | None = None
    origin: str | None = None
    birth_date: date | None = None
    buy_date: date | None = None
    sell_date: date | None = None


class AnimalSchema(AnimalBase):
    model_config = ConfigDict(from_attributes=True)
    breed_id: int | None
    father_id: int | None
    mother_id: int | None
    origin: str | None


class AnimalList(BaseModel):
    animals: list[AnimalSchema]


class AnimalWeightType(str, Enum):
    BIRTH = 'birth'
    WEANING = 'weaning'
    BUY = 'buy'
    SELL = 'sell'


class AnimalWeightCreateUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    weight_type: AnimalWeightType
    animal_tag: int
    weight: float
    weight_date: datetime


class AnimalWeightResponse(AnimalWeightCreateUpdate):
    id: int


class AnimalWeightList(BaseModel):
    animal_weights: list[AnimalWeightResponse]
