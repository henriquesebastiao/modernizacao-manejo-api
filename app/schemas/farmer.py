from pydantic import BaseModel, EmailStr


class FarmerCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str


class FarmerSchema(BaseModel):
    id: int | None
    user_id: int | None
    farmer_plan_id: int | None

    class Config:
        orm_mode = True
