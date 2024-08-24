from pydantic import BaseModel, ConfigDict


class EmploymentSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int | None
    user_id: int | None
    farmer_id: int | None
    farm_id: int | None
    employment_position_id: int | None


class EmploymentPositionSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int | None
    name: int | None
