from datetime import date

from pydantic import BaseModel


class PesagemBase(BaseModel):
    peso: float
    data: date


class PesagemCreate(PesagemBase):
    pass


class PesagemSerial(PesagemBase):
    id: int
    id_animal: int

    class Config:
        orm_mode = True
