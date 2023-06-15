from pydantic import BaseModel


class PropriedadeBase(BaseModel):
    nome: str
    fazendeiro_id: int


class PropriedadeCreateSchema(PropriedadeBase):
    ...


class PropriedadeUpdateSchema(PropriedadeBase):
    ...


class PropriedadeDeleteSchema(PropriedadeBase):
    ...


class PropriedadeSchema(PropriedadeBase):
    id: int
