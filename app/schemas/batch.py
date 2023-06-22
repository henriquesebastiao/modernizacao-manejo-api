from pydantic import BaseModel


class BatchSchema(BaseModel):
    id: int
    reg: str
    farm_id: int

    class Config:
        orm_mode = True
