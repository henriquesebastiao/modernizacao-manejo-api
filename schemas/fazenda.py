from pydantic import BaseModel


class FazendaBase(BaseModel):
    fazendeiro_id: int
    nome: str


class FazendaCreate(FazendaBase):
    pass


class FazendaSerial(FazendaBase):
    id: int

    class Config:
        orm_mode = True
