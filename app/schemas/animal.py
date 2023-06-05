"""Esquema de validação de dados para o modelo Animal."""

from datetime import date
from enum import Enum

from pydantic import BaseModel


class Sexo(str, Enum):
    """Lista de sexos dos quais o animal pode ser."""
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
    """Classe base para validação de dados de Animal."""
    chip: int | None
    brinco: int | None
    origem: str | None
    raca: Raca
    id_mae: int | None
    id_pai: int | None
    sexo: Sexo
    data_entrada: date
    data_nascimento: date


class AnimalCreate(AnimalBase):
    """Classe para validação de dados de criação de Animal."""
    peso: float


class Animal(AnimalBase):
    """Classe para validação de dados de Animal."""
    id: int  # O id é gerado automaticamente pelo banco de dados

    class Config:
        """Classe de configuração do Pydantic."""
        orm_mode = True
