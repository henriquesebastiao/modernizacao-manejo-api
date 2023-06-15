from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
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
