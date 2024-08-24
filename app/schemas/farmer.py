from pydantic import BaseModel


class FarmerCreate(BaseModel):
    user_id: int | None


class FarmerSchema(BaseModel):
    class Config:
        from_attributes = True

    id: int | None
    farmer_plan_id: int | None


class FarmerPlanSchema(BaseModel):
    class Config:
        from_attributes = True

    id: int | None
    plan: str | None
