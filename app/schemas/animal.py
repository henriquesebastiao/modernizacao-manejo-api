"""Esquema de validação de dados para o modelo Animal."""

from datetime import date
from enum import Enum

from pydantic import BaseModel

from app.schemas.lote import LoteSchema
from app.schemas.lote_log import LoteLogSchema
from app.schemas.peso_log import PesoLogSchema
from app.schemas.raca import RacaSchema


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
    mae_id: int | None
    pai_id: int | None
    sexo: Sexo | None
    data_entrada: date | None
    data_nascimento: date | None
    peso: float | None


class AnimalCreateSchema(AnimalSchemaBase):
    """Classe para validação de dados de criação de Animal."""


class AnimalUpdateSchema(AnimalSchemaBase):
    """Classe para validação de dados de atualização de Animal."""


class AnimalDeleteSchema(AnimalSchemaBase):
    """Classe para validação de dados de remoção de Animal."""


class AnimalSchema(AnimalSchemaBase):
    """Classe para validação de dados de atualização de Animal."""
    id: int
    lote: LoteSchema | None
    raca: RacaSchema | None
    peso_log: list[PesoLogSchema] | None
    lote_log: list[LoteLogSchema] | None

    class Config:
        """Configuração da classe."""
        orm_mode = True
