from pydantic import BaseModel

from app.utils import message


class BaseRaiseModel(BaseModel):
    detail: str


class EmailAlreadyExists(BaseRaiseModel):
    detail: str = message.AlreadyExists.EMAIL


class NotAuthorizedRegisterEmployee(BaseRaiseModel):
    detail: str = message.NotAuthorized.REGISTER_EMPLOYEE
