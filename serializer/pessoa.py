from pydantic import BaseModel


class PessoaBase(BaseModel):
    nome: str
    sobre_nome: str
    cargo_id: int


class PessoaCreate(PessoaBase):
    pass


class PessoaSerial(PessoaBase):
    id: int

    class Config:
        orm_mode = True
