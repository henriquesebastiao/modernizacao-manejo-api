from pydantic import BaseModel


class EmploymentSchema(BaseModel):
    id: int
    user_id: int
    farmer_id: int
    farm_id: int
    employment_position_id: int

    class Config:
        orm_mode = True
