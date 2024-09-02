from pydantic import BaseModel, ConfigDict

from app.models import FarmerPlan


class FarmerCreate(BaseModel):
    user_id: int
    farmer_plan: FarmerPlan


class FarmerSchema(FarmerCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int | None


class FarmerUpdate(BaseModel):
    farmer_plan: FarmerPlan


class FarmerList(BaseModel):
    farmers: list[FarmerSchema]
