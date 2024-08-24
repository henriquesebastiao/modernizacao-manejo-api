from pydantic import BaseModel


class UserTypeSchema(BaseModel):
    type: str


class UserTypePublic(UserTypeSchema):
    id: int

    class Config:
        from_attributes = True


class UserTypeList(BaseModel):
    user_types: list[UserTypePublic]
