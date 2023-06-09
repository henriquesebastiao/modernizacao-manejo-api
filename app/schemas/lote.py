from pydantic import BaseModel


class LoteBaseSchema(BaseModel):
    """Classe base para validação de dados de Lote."""
    nome: str
    numero: int
    dieta_id: int | None
    obs: str | None


class LoteCreateSchema(LoteBaseSchema):
    """Classe para validação de dados de criação de Lote."""


class LoteUpdateSchema(LoteBaseSchema):
    """Classe para validação de dados de atualização de Lote."""


class LoteDeleteSchema(LoteBaseSchema):
    """Classe para validação de dados de remoção de Lote."""


class LoteSchema(LoteBaseSchema):
    """Classe para validação de dados de atualização de Lote."""
    id: int

    class Config:
        """Configuração da classe."""
        orm_mode = True
