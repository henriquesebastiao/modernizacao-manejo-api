from pydantic import BaseModel


class PessoaBase(BaseModel):
    nome: str
    sobrenome: str | None
    cargo_id: int | None


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
