from pydantic import BaseModel


class UserTypeBase(BaseModel):
    type: str


class UserTypeCreate(UserTypeBase):
    pass


class UserTypeUpdate(UserTypeBase):
    pass


class UserTypeSchema(UserTypeBase):
    id: int | None

    class Config:
        orm_mode = True
