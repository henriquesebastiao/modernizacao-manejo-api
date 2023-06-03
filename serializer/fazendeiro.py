from pydantic import BaseModel


class FazendeiroBase(BaseModel):
    usuario_id: int


class FazendeiroCreate(FazendeiroBase):
    pass


class FazendeiroSerial(FazendeiroBase):
    id: int

    class Config:
        orm_mode = True
