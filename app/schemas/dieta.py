"""Esquema de validação de dados para o modelo Dieta."""

from pydantic import BaseModel


class DietaSchemaBase(BaseModel):
    """Classe base para validação de dados de Dieta."""
    nome: str | None
    descricao: str | None


class DietaCreateSchema(DietaSchemaBase):
    """Classe para validação de dados de criação de Dieta."""


class DietaUpdateSchema(DietaSchemaBase):
    """Classe para validação de dados de atualização de Dieta."""


class DietaDeleteSchema(DietaSchemaBase):
    """Classe para validação de dados de remoção de Dieta."""


class DietaSchema(DietaSchemaBase):
    """Classe para validação de dados de Dieta."""
    id: int

    class Config:
        """Classe de configuração do Pydantic."""
        orm_mode = True
