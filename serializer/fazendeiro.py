from pydantic import BaseModel


class Fazendeiro(BaseModel):
    id: int
    usuario_id: int
