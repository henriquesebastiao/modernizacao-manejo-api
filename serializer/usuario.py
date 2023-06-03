from pydantic import BaseModel


class UsuarioBase(BaseModel):
    email: str
    password: str
    pessoa_id: int


class UsuarioCreate(UsuarioBase):
    pass


class UsuarioSerial(UsuarioBase):
    id: int

    class Config:
        orm_mode = True
