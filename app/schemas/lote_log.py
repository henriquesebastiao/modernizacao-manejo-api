from datetime import date

from pydantic import BaseModel


class LoteLogBase(BaseModel):
    """Classe base para validação de dados de Lote."""
    lote_id: int | None
    data_entrada: date | None
    data_saida: date | None


class LoteLogCreate(LoteLogBase):
    """Classe para validação de dados de criação de Lote."""


class LoteLog(LoteLogBase):
    """Classe para validação de dados de atualização de Lote."""

    class Config:
        """Configuração da classe."""
        orm_mode = True
