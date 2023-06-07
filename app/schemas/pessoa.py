"""Esquema de validação de dados de Pessoa."""

from pydantic import BaseModel


class PessoaBaseSchema(BaseModel):
    """Classe base para validação de dados de Pessoa."""
    nome: str
    sobre_nome: str
    cargo_id: int


class PessoaCreateSchema(PessoaBaseSchema):
    """Classe para validação de dados de criação de Pessoa."""


class PessoaUpdateSchema(PessoaBaseSchema):
    """Classe para validação de dados de atualização de Pessoa."""


class PessoaDeleteSchema(PessoaBaseSchema):
    """Classe para validação de dados de remoção de Pessoa."""


class PessoaSchema(PessoaBaseSchema):
    """Classe para validação de dados de Pessoa."""
    id: int

    class Config:
        """Classe de configuração do Pydantic."""
        orm_mode = True
