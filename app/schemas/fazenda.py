"""Esquema de validação de dados da fazenda."""

from pydantic import BaseModel


class FazendaBase(BaseModel):
    """Classe base para validação de dados da fazenda."""
    fazendeiro_id: int
    nome: str


class FazendaCreate(FazendaBase):
    """Classe para validação de dados de criação da fazenda."""
    pass


class FazendaSerial(FazendaBase):
    """Classe para validação de dados da fazenda."""
    id: int

    class Config:
        """Classe de configuração do Pydantic."""
        orm_mode = True
