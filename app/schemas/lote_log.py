from datetime import date

from pydantic import BaseModel


class LoteLogBaseSchema(BaseModel):
    """Classe base para validação de dados de Lote."""
    lote_id: int | None
    data_entrada: date | None
    data_saida: date | None


class LoteLogCreateSchema(LoteLogBaseSchema):
    """Classe para validação de dados de criação de Lote."""


class LoteLogUpdateSchema(LoteLogBaseSchema):
    """Classe para validação de dados de atualização de Lote."""


class LoteLogDeleteSchema(LoteLogBaseSchema):
    """Classe para validação de dados de remoção de Lote."""


class LoteLogSchema(LoteLogBaseSchema):
    """Classe para validação de dados de atualização de Lote."""
    id: int

    class Config:
        """Configuração da classe."""
        orm_mode = True
