"""Esquema de validação de dados de Usuário."""

from pydantic import BaseModel


class UsuarioBaseSchema(BaseModel):
    """Classe base para validação de dados de Usuário."""
    email: str
    password: str
    pessoa_id: int


class UsuarioCreateSchema(UsuarioBaseSchema):
    """Classe para validação de dados de criação de Usuário."""


class UsuarioUpdateSchema(UsuarioBaseSchema):
    """Classe para validação de dados de atualização de Usuário."""


class UsuarioDeleteSchema(UsuarioBaseSchema):
    """Classe para validação de dados de remoção de Usuário."""


class UsuarioSchema(UsuarioBaseSchema):
    """Classe para validação de dados de Usuário."""
    id: int

    class Config:
        orm_mode = True
