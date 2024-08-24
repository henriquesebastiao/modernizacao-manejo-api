from datetime import datetime

from pydantic import BaseModel


class BatchSchema(BaseModel):
    class Config:
        from_attributes = True

    id: int | None
    reg: str | None
    farm_id: int | None


class BatchLogSchema(BaseModel):
    class Config:
        from_attributes = True

    id: int | None
    batch_id: int | None
    animal_id: int | None
    entry_date: datetime | None
    departure_date: datetime | None
