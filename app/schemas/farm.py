from pydantic import BaseModel


class FarmSchema(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
