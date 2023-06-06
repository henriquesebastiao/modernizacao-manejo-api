"""Esquema validação de dados para o modelo Peso Log."""

from datetime import date

from pydantic import BaseModel


class PesoLogBase(BaseModel):
    """Classe base para validação de dados de Peso Log."""
    data: date
    peso: float


class PesoLogCreate(PesoLogBase):
    """Classe para validação de dados de criação de Peso Log."""
    animal_id: int


class PesoLog(PesoLogBase):
    """Classe para validação de dados de atualização de Peso Log."""

    class Config:
        """Configuração da classe."""
        orm_mode = True
