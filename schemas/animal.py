from datetime import date
from enum import Enum

from pydantic import BaseModel


class Sexo(str, Enum):
    macho = "Macho"
    femea = "Fêmea"


class Raca(str, Enum):
    """Lista de raças das quais o animal pode ser."""
    nelore = "Nelore"
    angus = "Angus"
    guzera = "Guzerá"
    senepol = "Senepol"
    outra = "Outra"


class AnimalBase(BaseModel):
    chip: int | None
    brinco: int | None
    origem: str
    raca: Raca
    id_mae: int
    id_pai: int
    sexo: Sexo
    data_entrada: date
    data_nascimento: date
    peso_nascimento: float


class AnimalCreate(AnimalBase):
    pass


class Animal(AnimalBase):
    id: int  # O id é gerado automaticamente pelo banco de dados

    class Config:
        orm_mode = True
