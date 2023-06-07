"""Esquema de validação de dados da fazenda."""

from pydantic import BaseModel


class FazendaSchemaBase(BaseModel):
    """Classe base para validação de dados da fazenda."""
    fazendeiro_id: int
    nome: str


class FazendaCreateSchema(FazendaSchemaBase):
    """Classe para validação de dados de criação da fazenda."""


class FazendaUpdateSchema(FazendaSchemaBase):
    """Classe para validação de dados de atualização da fazenda."""


class FazendaDeleteSchema(FazendaSchemaBase):
    """Classe para validação de dados de remoção da fazenda."""


class FazendaSchema(FazendaSchemaBase):
    """Classe para validação de dados da fazenda."""
    id: int

    class Config:
        """Classe de configuração do Pydantic."""
        orm_mode = True
