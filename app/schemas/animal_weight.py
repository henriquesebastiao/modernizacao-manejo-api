from datetime import datetime

from pydantic import BaseModel


class AnimalWeightSchema(BaseModel):
    id: int | None
    weight_type_id: str | None
    animal_id: int | None
    weight: float | None
    weight_date: datetime | None

    class Config:
        orm_mode = True
