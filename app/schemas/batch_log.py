from datetime import datetime

from pydantic import BaseModel


class BatchLogSchema(BaseModel):
    id: int | None
    batch_id: int | None
    animal_id: int | None
    entry_date: datetime | None
    departure_date: datetime | None

    class Config:
        from_attributes = True
