from pydantic import BaseModel, EmailStr


class LoginSchema(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True
