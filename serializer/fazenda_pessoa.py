from pydantic import BaseModel


class FazendaPessoaBase(BaseModel):
    fazenda_id: int
    pessoa_id: int


class FazendaPessoaCreate(FazendaPessoaBase):
    pass


class FazendaPessoaSerial(FazendaPessoaBase):
    id: int

    class Config:
        orm_mode = True
