from app.services.base import BaseService

from app.models.user import User


class UserService(BaseService):
    def __init__(self):
        super().__init__(User)
