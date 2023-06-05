"""Esquema de validação de dados do fazendeiro."""

from pydantic import BaseModel


class FazendeiroBase(BaseModel):
    usuario_id: int


class FazendeiroCreate(FazendeiroBase):
    pass


class FazendeiroSerial(FazendeiroBase):
    id: int

    class Config:
        """Classe de configuração do Pydantic."""
        orm_mode = True
