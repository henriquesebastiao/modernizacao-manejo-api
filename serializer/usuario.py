from pydantic import BaseModel


class Usuario(BaseModel):
    id: int
    email: str
    password: str
    pessoa_id: int
