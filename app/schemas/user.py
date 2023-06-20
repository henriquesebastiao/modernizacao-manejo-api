from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    phone: str


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    password: str


class UserDelete(UserBase):
    ...


class UserSchema(UserBase):

    class Config:
        orm_mode = True
