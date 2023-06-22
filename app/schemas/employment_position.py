from pydantic import BaseModel


class EmploymentPositionSchema(BaseModel):
    id: int | None
    name: int | None

    class Config:
        orm_mode = True
