"""Esquema de validação de dados de Usuário."""

from pydantic import BaseModel


class UsuarioBase(BaseModel):
    """Classe base para validação de dados de Usuário."""
    email: str
    password: str
    pessoa_id: int


class UsuarioCreate(UsuarioBase):
    """Classe para validação de dados de criação de Usuário."""
    pass


class Usuario(UsuarioBase):
    """Classe para validação de dados de Usuário."""
    id: int

    class Config:
        orm_mode = True
