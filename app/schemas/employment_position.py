from pydantic import BaseModel


class EmploymentPositionSchema(BaseModel):
    id: int
    name: int

    class Config:
        orm_mode = True
