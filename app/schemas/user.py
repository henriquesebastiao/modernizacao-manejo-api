from datetime import datetime

from pydantic import BaseModel, EmailStr, Field

from app.utils.type import T_PhoneNumberBR

FIELD_PHONE_NUMBER = Field(default=None, examples=['66999999999'])


class UserBase(BaseModel):
    first_name: str
    last_name: str | None = None
    email: EmailStr


class UserCreate(UserBase):
    password: str
    phone: T_PhoneNumberBR | None = FIELD_PHONE_NUMBER


class SubordinateUserCreate(UserCreate):
    manager_id: int


class UserUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    email: EmailStr | None = None
    phone: T_PhoneNumberBR | None = FIELD_PHONE_NUMBER
    password: str | None = None
    active: bool | None = None


class UserSchema(UserBase):
    id: int
    phone: T_PhoneNumberBR | None = FIELD_PHONE_NUMBER
    created_at: datetime
    updated_at: datetime
    manager_id: int | None = None
    active: bool


class SubordinateUserSchema(UserSchema):
    manager_id: int


class UserList(BaseModel):
    users: list[UserSchema]
