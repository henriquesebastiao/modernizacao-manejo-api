from pydantic import BaseModel


class LoteBase(BaseModel):
    nome: str
    numero: int
    dieta_id: int | None
    obs: str | None


class LoteCreate(LoteBase):
    ...


class LoteUpdate(LoteBase):
    ...


class LoteDelete(LoteBase):
    ...


class LoteSchema(LoteBase):
    id: int
