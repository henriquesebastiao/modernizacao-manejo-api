from pydantic import BaseModel


class FarmSchema(BaseModel):
    id: int | None
    name: str | None

    class Config:
        orm_mode = True
