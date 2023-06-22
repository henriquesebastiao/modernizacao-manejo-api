from pydantic import BaseModel


class FarmerSchema(BaseModel):
    id: int | None
    user_id: int | None
    farmer_plan_id: int | None

    class Config:
        orm_mode = True
