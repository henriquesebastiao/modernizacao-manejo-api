from datetime import date
from pydantic import BaseModel


class PesagemBase(BaseModel):
    peso: float
    data: date
    id_animal: int


class PesagemCreate(PesagemBase):
    pass


class PesagemSerial(PesagemBase):
    id: int

    class Config:
        orm_mode = True
