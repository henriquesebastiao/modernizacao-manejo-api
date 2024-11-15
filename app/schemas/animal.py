from datetime import date

from pydantic import BaseModel

from app.utils.enum import Breeds, Genders, WeightTypes


class AnimalCreate(BaseModel):
    tag: int
    gender: Genders
    origin: str | None = None
    sisbov: int | None = None
    breed: Breeds
    father_id: int | None = None
    mother_id: int | None = None
    birth_date: date | None = None
    buy_date: date | None = None


class AnimalUpdate(BaseModel):
    tag: int | None = None
    gender: Genders | None = None
    origin: str | None = None
    sisbov: int | None = None
    breed: Breeds | None = None
    father_id: int | None = None
    mother_id: int | None = None
    birth_date: date | None = None
    buy_date: date | None = None
    sell_date: date | None = None


class AnimalSchema(BaseModel):
    tag: int | None
    gender: Genders | None
    origin: str | None
    sisbov: int | None
    breed: Breeds | None
    father_id: int | None
    mother_id: int | None
    birth_date: date | None
    buy_date: date | None
    sell_date: date | None


class AnimalList(BaseModel):
    animals: list[AnimalSchema]


class AnimalWeightCreate(BaseModel):
    weight_type: WeightTypes
    animal_id: int
    weight: float
    weight_date: date


class AnimalWeightUpdate(BaseModel):
    weight_type: WeightTypes | None = None
    animal_tag: int | None = None
    weight: float | None = None
    weight_date: date | None = None


class AnimalWeightResponse(AnimalWeightCreate):
    id: int


class AnimalWeightResponseForList(BaseModel):
    weight_type: WeightTypes | None
    animal_tag: int | None
    weight: float | None
    weight_date: date | None


class AnimalWeightList(BaseModel):
    animal_weights: list[AnimalWeightResponseForList]
