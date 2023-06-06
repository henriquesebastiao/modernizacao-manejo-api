"""Esquema validação de dados para o modelo Pesagem."""

from datetime import date

from pydantic import BaseModel


class PesagemBase(BaseModel):
    """Classe base para validação de dados de Pesagem."""
    data: date
    peso: float


class PesagemCreate(PesagemBase):
    """Classe para validação de dados de criação de Pesagem."""
    animal_id: int


class Pesagem(PesagemBase):
    """Classe para validação de dados de atualização de Pesagem."""

    class Config:
        """Configuração da classe."""
        orm_mode = True
