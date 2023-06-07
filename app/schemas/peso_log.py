"""Esquema validação de dados para o modelo Peso Log."""

from datetime import date

from pydantic import BaseModel


class PesoLogBaseSchema(BaseModel):
    """Classe base para validação de dados de Peso Log."""
    data: date
    peso: float


class PesoLogCreateSchema(PesoLogBaseSchema):
    """Classe para validação de dados de criação de Peso Log."""
    animal_id: int


class PesoLogUpdateSchema(PesoLogBaseSchema):
    """Classe para validação de dados de atualização de Peso Log."""


class PesoLogDeleteSchema(PesoLogBaseSchema):
    """Classe para validação de dados de remoção de Peso Log."""


class PesoLogSchema(PesoLogBaseSchema):
    """Classe para validação de dados de atualização de Peso Log."""

    class Config:
        """Configuração da classe."""
        orm_mode = True
