from pydantic import BaseModel


class CargoBase(BaseModel):
    nome: str


class CargoCreate(CargoBase):
    ...


class CargoUpdate(CargoBase):
    ...


class CargoDelete(CargoBase):
    ...


class CargoSchema(CargoBase):
    id: int

    class Config:
        orm_mode = True
