from app.services.base import BaseService

from app.models.user import User


class LoginService(BaseService):
    def __init__(self):
        super().__init__(User)

    def login(self, user):
        user = self.get_by_field("email", user.email)
        if user.password == user.password:
            return user
