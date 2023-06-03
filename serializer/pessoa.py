from pydantic import BaseModel


class Pessoa(BaseModel):
    id: int
    nome: str
    sobre_nome: str
    cargo_id: int
