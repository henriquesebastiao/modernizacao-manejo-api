from pydantic import BaseModel


class DietaBase(BaseModel):
    nome: str | None
    desc: str | None


class DietaCreate(DietaBase):
    ...


class DietaUpdate(DietaBase):
    ...


class DietaDelete(DietaBase):
    ...


class DietaSchema(DietaBase):
    id: int

    class Config:
        orm_mode = True
