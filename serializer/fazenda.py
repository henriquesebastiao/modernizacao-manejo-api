from pydantic import BaseModel


class Fazenda(BaseModel):
    id: int
    fazendeiro_id: int
    nome: str
