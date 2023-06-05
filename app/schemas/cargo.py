from pydantic import BaseModel


class CargoBase(BaseModel):
    nome: str


class CargoCreate(CargoBase):
    pass


class CargoSerial(CargoBase):
    id: int

    class Config:
        orm_mode = True
