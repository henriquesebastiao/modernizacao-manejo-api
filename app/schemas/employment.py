from pydantic import BaseModel


class EmploymentSchema(BaseModel):
    class Config:
        from_attributes = True

    id: int | None
    user_id: int | None
    farmer_id: int | None
    farm_id: int | None
    employment_position_id: int | None


class EmploymentPositionSchema(BaseModel):
    class Config:
        from_attributes = True

    id: int | None
    name: int | None
