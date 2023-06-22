from pydantic import BaseModel


class UserTypeSchema(BaseModel):
    id: int
    type: str

    class Config:
        orm_mode = True
