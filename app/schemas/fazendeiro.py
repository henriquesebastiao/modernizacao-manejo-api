from pydantic import BaseModel


class FazendeiroBase(BaseModel):
    ...


class FazendeiroCreate(FazendeiroBase):
    nome: str
    password: str
    email: str


class FazendeiroUpdate(FazendeiroBase):
    ...


class FazendeiroDelete(FazendeiroBase):
    ...


class FazendeiroSchema(FazendeiroBase):
    id: int

    class Config:
        orm_mode = True
