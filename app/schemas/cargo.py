"""Esquema de validação de dados para o modelo Cargo."""

from pydantic import BaseModel


class CargoSchemaBase(BaseModel):
    """Classe base para validação de dados de Cargo."""
    nome: str


class CargoCreateSchema(CargoSchemaBase):
    """Classe para validação de dados de criação de Cargo."""


class CargoUpdateSchema(CargoSchemaBase):
    """Classe para validação de dados de atualização de Cargo."""


class CargoDeleteSchema(CargoSchemaBase):
    """Classe para validação de dados de remoção de Cargo."""


class CargoSchema(CargoSchemaBase):
    """Classe para validação de dados de Cargo."""
    id: int

    class Config:
        """Classe de configuração do Pydantic."""
        orm_mode = True
