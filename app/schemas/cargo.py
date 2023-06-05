"""Esquema de validação de dados para o modelo Cargo."""

from pydantic import BaseModel


class CargoBase(BaseModel):
    """Classe base para validação de dados de Cargo."""
    nome: str


class CargoCreate(CargoBase):
    """Classe para validação de dados de criação de Cargo."""
    pass


class CargoSerial(CargoBase):
    """Classe para validação de dados de Cargo."""
    id: int

    class Config:
        """Classe de configuração do Pydantic."""
        orm_mode = True
