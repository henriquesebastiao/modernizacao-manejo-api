"""Esquema de validação de dados de Usuário."""

from pydantic import BaseModel


class UserBaseSchema(BaseModel):
    """Classe base para validação de dados de Usuário."""
    email: str
    password: str


class UserLoginSchema(BaseModel):
    """Classe base para validação de dados de Usuário."""
    email: str
    password: str


class UserCreateSchema(UserBaseSchema):
    """Classe para validação de dados de criação de Usuário."""


class UserUpdateSchema(UserBaseSchema):
    """Classe para validação de dados de atualização de Usuário."""


class UserDeleteSchema(UserBaseSchema):
    """Classe para validação de dados de remoção de Usuário."""


class UserSchema(UserBaseSchema):
    """Classe para validação de dados de Usuário."""
    id: int

    class Config:
        orm_mode = True
