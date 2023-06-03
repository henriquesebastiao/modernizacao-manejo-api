from pydantic import BaseModel
from datetime import date


class AnimalSerializer(BaseModel):
    id: int
    origem: str
    id_mae: int
    id_pai: int
    idade: int
    sexo: str
    data_entrada: date
    peso_nascimento: float
