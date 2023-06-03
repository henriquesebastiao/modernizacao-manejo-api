from pydantic import BaseModel
from datetime import date


class Animal(BaseModel):
    id: int | None
    origem: str | None
    id_mae: int
    id_pai: int
    idade: int
    sexo: str
    data_entrada: date
    peso_nascimento: int
