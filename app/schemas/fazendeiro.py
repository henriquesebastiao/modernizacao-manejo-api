from pydantic import BaseModel, EmailStr


class FazendeiroBase(BaseModel):
    ...


class FazendeiroCreate(FazendeiroBase):
    nome: str
    password: str
    email: EmailStr


class FazendeiroUpdate(FazendeiroBase):
    ...


class FazendeiroDelete(FazendeiroBase):
    ...


class FazendeiroSchema(FazendeiroBase):
    id: int

    class Config:
        orm_mode = True
