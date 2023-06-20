from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    phone: str


class UserCreate(UserBase):
    ...


class UserUpdate(UserBase):
    ...


class UserDelete(UserBase):
    ...


class UserSchema(UserBase):

    class Config:
        orm_mode = True
