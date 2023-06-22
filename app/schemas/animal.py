from datetime import date
from enum import Enum

from pydantic import BaseModel


class Sexo(str, Enum):
    M = "Macho"
    F = "Fêmea"


class AnimalSchema(BaseModel):
    id: int | None
    tag: int | None
    sisbov: int | None
    gender: Sexo | None
    breed_id: int | None
    father_id: int | None
    mother_id: int | None
    origin_id: int | None
    birth_date: date | None
    buy_date: date | None
    sell_date: date | None

    class Config:
        orm_mode = True
