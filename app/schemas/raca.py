"""Esquema de validação de dados para o modelo Raca."""

from pydantic import BaseModel


class RacaBaseSchema(BaseModel):
    """Classe base para validação de dados de Raca."""
    nome: str


class RacaCreateSchema(RacaBaseSchema):
    """Classe para validação de dados de criação de Raca."""


class RacaUpdateSchema(RacaBaseSchema):
    """Classe para validação de dados de atualização de Raca."""


class RacaDeleteSchema(RacaBaseSchema):
    """Classe para validação de dados de remoção de Raca."""


class RacaSchema(RacaBaseSchema):
    """Classe para validação de dados de atualização de Raca."""
    id: int

    class Config:
        """Configuração da classe."""
        orm_mode = True
