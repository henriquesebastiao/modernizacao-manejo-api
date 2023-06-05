"""Esquema de validação de dados de Pessoa."""

from pydantic import BaseModel


class PessoaBase(BaseModel):
    """Classe base para validação de dados de Pessoa."""
    nome: str
    sobre_nome: str
    cargo_id: int


class PessoaCreate(PessoaBase):
    """Classe para validação de dados de criação de Pessoa."""
    pass


class PessoaSerial(PessoaBase):
    """Classe para validação de dados de Pessoa."""
    id: int

    class Config:
        """Classe de configuração do Pydantic."""
        orm_mode = True
