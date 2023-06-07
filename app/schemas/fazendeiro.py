"""Esquema de validação de dados do fazendeiro."""

from pydantic import BaseModel


class FazendeiroBaseSchema(BaseModel):
    usuario_id: int


class FazendeiroCreateSchema(FazendeiroBaseSchema):
    """Classe para validação de dados de criação do fazendeiro."""


class FazendeiroUpdateSchema(FazendeiroBaseSchema):
    """Classe para validação de dados de atualização do fazendeiro."""


class FazendeiroDeleteSchema(FazendeiroBaseSchema):
    """Classe para validação de dados de remoção do fazendeiro."""


class FazendeiroSchema(FazendeiroBaseSchema):
    id: int

    class Config:
        """Classe de configuração do Pydantic."""
        orm_mode = True
