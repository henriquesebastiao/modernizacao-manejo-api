from pydantic import BaseModel


class FarmerPlanSchema(BaseModel):
    id: int
    plan: str

    class Config:
        orm_mode = True
