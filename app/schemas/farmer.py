from pydantic import BaseModel


class FarmerSchema(BaseModel):
    id: int
    user_id: int
    farmer_plan_id: int

    class Config:
        orm_mode = True
