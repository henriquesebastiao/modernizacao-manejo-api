from datetime import datetime

from pydantic import BaseModel


class AnimalWeightSchema(BaseModel):
    id: int
    weight_type_id: str
    animal_id: int
    weight: float
    weight_date: datetime

    class Config:
        orm_mode = True
