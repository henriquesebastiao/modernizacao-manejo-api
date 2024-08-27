from datetime import datetime

from pydantic import BaseModel, ConfigDict


class BatchSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int | None
    reg: str | None
    farm_id: int | None


class BatchList(BaseModel):
    batchs: list[BatchSchema]


class BatchLogSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int | None
    batch_id: int | None
    animal_id: int | None
    entry_date: datetime | None
    departure_date: datetime | None


class BatchLogList(BaseModel):
    batch_logs: list[BatchLogSchema]
