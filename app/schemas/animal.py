"""Esquema de validação de dados para o modelo Animal."""

from datetime import date
from enum import Enum

from pydantic import BaseModel

from app.schemas.lote import Lote
from app.schemas.lote_log import LoteLog
from app.schemas.peso_log import PesoLog
from app.schemas.raca import Raca


class Sexo(str, Enum):
    """Lista de sexos dos quais o animal pode ser."""
    macho = "Macho"
    femea = "Fêmea"


class AnimalSchemaBase(BaseModel):
    """Classe base para validação de dados de Animal."""
    chip: str | None
    brinco: str | None
    origem: str | None
    raca_id: int | None
    id_mae: int | None
    id_pai: int | None
    sexo: Sexo
    data_entrada: date
    data_nascimento: date
    peso: float


class AnimalCreateSchema(AnimalSchemaBase):
    """Classe para validação de dados de criação de Animal."""


class AnimalUpdateSchema(AnimalSchemaBase):
    """Classe para validação de dados de atualização de Animal."""


class AnimalDeleteSchema(AnimalSchemaBase):
    """Classe para validação de dados de atualização de Animal."""
    id: int


class AnimalSchema(AnimalSchemaBase):
    """Classe para validação de dados de atualização de Animal."""
    lote: Lote
    raca: Raca
    peso_log: list[PesoLog]
    lote_log: list[LoteLog]

    class Config:
        """Configuração da classe."""
        orm_mode = True
