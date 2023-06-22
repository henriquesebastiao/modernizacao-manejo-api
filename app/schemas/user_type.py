from pydantic import BaseModel


class UserTypeSchema(BaseModel):
    id: int | None
    type: str | None

    class Config:
        orm_mode = True
