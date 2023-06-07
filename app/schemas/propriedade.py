"""Esquema de validação de dados de Propriedade."""

from pydantic import BaseModel


class PropriedadeBaseSchema(BaseModel):
    """Classe base para validação de dados de Propriedade."""
    nome: str
    fazendeiro_id: int


class PropriedadeCreateSchema(PropriedadeBaseSchema):
    """Classe para validação de dados de criação de Propriedade."""


class PropriedadeUpdateSchema(PropriedadeBaseSchema):
    """Classe para validação de dados de atualização de Propriedade."""


class PropriedadeDeleteSchema(PropriedadeBaseSchema):
    """Classe para validação de dados de remoção de Propriedade."""


class PropriedadeSchema(PropriedadeBaseSchema):
    """Classe para validação de dados de Propriedade."""
    id: int

    class Config:
        """Classe de configuração do Pydantic."""
        orm_mode = True
