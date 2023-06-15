from pydantic import BaseModel


class PropriedadeBase(BaseModel):
    nome: str
    fazendeiro_id: int


class PropriedadeCreate(PropriedadeBase):
    ...


class PropriedadeUpdate(PropriedadeBase):
    ...


class PropriedadeDelete(PropriedadeBase):
    ...


class PropriedadeSchema(PropriedadeBase):
    id: int

    class Config:
        orm_mode = True
