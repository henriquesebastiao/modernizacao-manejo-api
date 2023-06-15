from datetime import date
from enum import Enum

from pydantic import BaseModel

from app.schemas.lote import LoteSchema
from app.schemas.lote_log import LoteLogSchema
from app.schemas.peso_log import PesoLogSchema
from app.schemas.raca import RacaSchema


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


class AnimalCreateSchema(AnimalBase):
    ...


class AnimalUpdateSchema(AnimalBase):
    ...


class AnimalSchema(AnimalBase):
    id: int | None
    lote: LoteSchema | None
    raca: RacaSchema | None
    peso_log: list[PesoLogSchema] | None
    lote_log: list[LoteLogSchema] | None
