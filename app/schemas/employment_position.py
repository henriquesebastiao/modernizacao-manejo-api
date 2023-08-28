from pydantic import BaseModel


class EmploymentPositionSchema(BaseModel):
    id: int | None
    name: int | None

    class Config:
        from_attributes = True
