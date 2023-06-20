from pydantic import BaseModel


class CargoBase(BaseModel):
    nome: str


class CargoCreate(CargoBase):
    user_id: int


class CargoUpdate(CargoBase):
    ...


class CargoSchema(CargoBase):

    class Config:
        orm_mode = True
