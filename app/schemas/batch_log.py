from datetime import datetime

from pydantic import BaseModel


class BatchLogSchema(BaseModel):
    id: int
    batch_id: int
    animal_id: int
    entry_date: datetime
    departure_date: datetime

    class Config:
        orm_mode = True
