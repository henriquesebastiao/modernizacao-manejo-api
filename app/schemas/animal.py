from datetime import date
from enum import Enum

from pydantic import BaseModel



class Sexo(str, Enum):
    m = "Macho"
    f = "Fêmea"


class AnimalBase(BaseModel):
    chip: str | None
    brinco: str | None
    origem: str | None
    raca_id: int | None
    mae_id: int | None
    pai_id: int | None
    sexo: Sexo | None
    data_entrada: date | None
    data_nascimento: date | None
    peso: float | None


class AnimalCreate(AnimalBase):
    ...


class AnimalUpdate(AnimalBase):
    ...


class AnimalSchema(AnimalBase):
    id: int | None

    class Config:
        orm_mode = True
