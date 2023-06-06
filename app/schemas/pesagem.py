"""Esquema validação de dados para o modelo Pesagem."""

from datetime import date

from pydantic import BaseModel


class PesagemBase(BaseModel):
    """Classe base para validação de dados de Pesagem."""
    animal_id: int
    peso: float
    data: date


class PesagemCreate(PesagemBase):
    """Classe para validação de dados de criação de Pesagem."""
