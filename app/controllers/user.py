from app.controllers.base import BaseControllers

from app.models.user import User


class UserController(BaseControllers):
    def __init__(self):
        super().__init__(User)
