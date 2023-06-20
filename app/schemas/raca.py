from pydantic import BaseModel


class RacaBase(BaseModel):
    nome: str


class RacaCreate(RacaBase):
    ...


class RacaUpdate(RacaBase):
    ...


class RacaDelete(RacaBase):
    ...


class RacaSchema(RacaBase):

    class Config:
        orm_mode = True
