from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    password: str


class UserCreate(UserBase):
    ...


class UserUpdate(UserBase):
    ...


class UserDelete(UserBase):
    ...


class UserSchema(UserBase):
    id: int

    class Config:
        orm_mode = True
