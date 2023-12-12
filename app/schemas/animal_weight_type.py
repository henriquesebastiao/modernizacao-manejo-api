from pydantic import BaseModel


class AnimalWeightTypeSchema(BaseModel):
    id: int | None
    type: str | None

    class Config:
        from_attributes = True
