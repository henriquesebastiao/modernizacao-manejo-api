from datetime import date

from pydantic import BaseModel


class PesoLogBase(BaseModel):
    data: date
    peso: float


class PesoLogCreate(PesoLogBase):
    animal_id: int


class PesoLogUpdate(PesoLogBase):
    ...


class PesoLogDelete(PesoLogBase):
    ...


class PesoLogSchema(PesoLogBase):
    id: int

    class Config:
        orm_mode = True
