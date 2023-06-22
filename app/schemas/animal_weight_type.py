from pydantic import BaseModel


class AnimalWeightTypeSchema(BaseModel):
    id: int
    type: str

    class Config:
        orm_mode = True
