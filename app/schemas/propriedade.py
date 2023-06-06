"""Esquema de validação de dados de Propriedade."""

from pydantic import BaseModel


class PropriedadeBase(BaseModel):
    """Classe base para validação de dados de Propriedade."""
    nome: str
    fazendeiro_id: int


class PropriedadeCreate(PropriedadeBase):
    """Classe para validação de dados de criação de Propriedade."""
    pass


class PropriedadeSerial(PropriedadeBase):
    """Classe para validação de dados de Propriedade."""
    id: int

    class Config:
        """Classe de configuração do Pydantic."""
        orm_mode = True
