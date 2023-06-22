from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    id: int | None
    first_name: str | None
    last_name: str | None
    phone: str | None
    email: EmailStr
    password: str
    create_at: datetime = datetime.now()
    update_at: datetime = datetime.now()
    user_type_id: int | None
    manager_id: int | None
    active: bool = True

    class Config:
        orm_mode = True
