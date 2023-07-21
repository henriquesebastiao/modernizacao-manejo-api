from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    phone: str | None
    password: str | None
    active: bool | None


class UserSchema(UserBase):
    id: int | None
    phone: str | None
    create_at: datetime | None = datetime.now()
    update_at: datetime | None = datetime.now()
    user_type_id: int | None
    manager_id: int | None
    active: bool | None = True

    class Config:
        orm_mode = True
