from pydantic import BaseModel


class BreedSchema(BaseModel):
    id: int | None
    name: str | None

    class Config:
        from_attributes = True
