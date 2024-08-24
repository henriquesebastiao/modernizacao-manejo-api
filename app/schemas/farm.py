from pydantic import BaseModel


class FarmSchema(BaseModel):
    class Config:
        from_attributes = True

    id: int | None
    name: str | None
