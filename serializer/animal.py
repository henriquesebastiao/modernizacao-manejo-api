from datetime import date
from enum import Enum

from pydantic import BaseModel


class Sexo(str, Enum):
    macho = "Macho"
    femea = "Fêmea"


class AnimalBase(BaseModel):
    chip: int
    brinco: int
    origem: str
    id_mae: int
    id_pai: int
    idade: int
    sexo: Sexo
    data_entrada: date
    peso_nascimento: float


class AnimalCreate(AnimalBase):
    pass


class AnimalSerial(AnimalBase):
    id: int

    class Config:
        orm_mode = True
