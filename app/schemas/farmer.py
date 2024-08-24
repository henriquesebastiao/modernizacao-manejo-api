from pydantic import BaseModel, ConfigDict


class FarmerCreate(BaseModel):
    user_id: int | None


class FarmerSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int | None
    farmer_plan_id: int | None


class FarmerPlanSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int | None
    plan: str | None
