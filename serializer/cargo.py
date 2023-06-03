from pydantic import BaseModel


class Cargo(BaseModel):
    id: int
    nome: str
