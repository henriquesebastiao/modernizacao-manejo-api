from pydantic import BaseModel


class BatchSchema(BaseModel):
    id: int | None
    reg: str | None
    farm_id: int | None

    class Config:
        from_attributes = True
