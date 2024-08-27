from pydantic import BaseModel, ConfigDict


class FarmerCreate(BaseModel):
    user_id: int | None


class FarmerSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int | None
    farmer_plan_id: int | None


class FarmerList(BaseModel):
    farmers: list[FarmerSchema]


class FarmerPlanSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int | None
    plan: str | None


class FarmerPlanList(BaseModel):
    farmer_plans: list[FarmerPlanSchema]
