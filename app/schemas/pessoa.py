from pydantic import BaseModel


class PessoaBase(BaseModel):
    nome: str
    sobre_nome: str
    cargo_id: int


class PessoaCreate(PessoaBase):
    ...


class PessoaUpdate(PessoaBase):
    ...


class PessoaDelete(PessoaBase):
    ...


class PessoaSchema(PessoaBase):
    id: int

    class Config:
        orm_mode = True
