from pydantic import BaseModel, EmailStr


class LoginBase(BaseModel):
    email: EmailStr
    password: str


class LoginSchema(LoginBase):
    class Config:
        orm_mode = True
