from pydantic import BaseModel


class CargoSerializer(BaseModel):
    id: int
    nome: str
