"""Esquema de validação de dados para o modelo Raca."""

from pydantic import BaseModel


class RacaBase(BaseModel):
    """Classe base para validação de dados de Raca."""
    nome: str


class RacaCreate(RacaBase):
    """Classe para validação de dados de criação de Raca."""
    pass


class Raca(RacaBase):
    """Classe para validação de dados de atualização de Raca."""
    id: int

    class Config:
        """Configuração da classe."""
        orm_mode = True
