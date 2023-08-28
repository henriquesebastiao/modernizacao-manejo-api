from pydantic import BaseModel


class FarmerPlanSchema(BaseModel):
    id: int | None
    plan: str | None

    class Config:
        from_attributes = True
