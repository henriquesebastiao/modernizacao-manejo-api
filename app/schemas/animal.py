"""Esquema de validação de dados para o modelo Animal."""

from datetime import date
from enum import Enum

from pydantic import BaseModel

from app.schemas.lote import Lote
from app.schemas.lote_log import LoteLog
from app.schemas.peso_log import PesoLog


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
    chip: str | None
    brinco: str | None
    origem: str | None
    raca: Raca
    id_mae: int | None
    id_pai: int | None
    sexo: Sexo
    data_entrada: date
    data_nascimento: date
    peso: float
    lote_id: int


class AnimalCreate(AnimalBase):
    """Classe para validação de dados de criação de Animal."""


class Animal(AnimalBase):
    """Classe para validação de dados de atualização de Animal."""
    lote: Lote
    peso_log: list[PesoLog]
    lote_log: list[LoteLog]

    class Config:
        """Configuração da classe."""
        orm_mode = True
