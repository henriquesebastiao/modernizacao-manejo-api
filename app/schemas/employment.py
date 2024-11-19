from pydantic import BaseModel, ConfigDict

from app.utils.enum import EmploymentPositions


class EmploymentCreate(BaseModel):
    user_id: int | None
    farmer_id: int | None
    farm_id: int | None
    employment_position: EmploymentPositions | None


class EmploymentSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int | None
    user_id: int | None
    farmer_id: int | None
    farm_id: int | None
    employment_position: EmploymentPositions | None


class EmploymentList(BaseModel):
    employments: list[EmploymentSchema]
