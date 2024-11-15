from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    first_name: str
    last_name: str | None = None
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    email: EmailStr | None = None
    phone: str | None = None
    password: str | None = None
    active: bool | None = None


class UserSchema(UserBase):
    id: int
    phone: str | None = None
    created_at: datetime
    updated_at: datetime
    manager_id: int | None = None
    active: bool


class UserList(BaseModel):
    users: list[UserSchema]
