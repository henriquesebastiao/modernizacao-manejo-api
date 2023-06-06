from pydantic import BaseModel


class LoteBase(BaseModel):
    """Classe base para validação de dados de Lote."""
    nome: str
    descricao: str | None
    referencia: str | None
    numero: int


class LoteCreate(LoteBase):
    """Classe para validação de dados de criação de Lote."""


class Lote(LoteBase):
    """Classe para validação de dados de atualização de Lote."""

    class Config:
        """Configuração da classe."""
        orm_mode = True