from pydantic import BaseModel


class FarmerCreate(BaseModel):
    user_id: int | None


class FarmerSchema(BaseModel):
    id: int | None
    farmer_plan_id: int | None

    class Config:
        orm_mode = True
