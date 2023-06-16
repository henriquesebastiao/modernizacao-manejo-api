from datetime import date

from pydantic import BaseModel


class PesoLogBase(BaseModel):
    data: date
    peso: float


class PesoLogCreate(PesoLogBase):
    ref: str


class PesoLogUpdate(PesoLogBase):
    ...


class PesoLogDelete(PesoLogBase):
    ...


class PesoLogSchema(PesoLogBase):
    id: int

    class Config:
        orm_mode = True
