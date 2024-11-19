from enum import Enum


class AlreadyExists(str, Enum):
    __complement = ' already exists'

    EMAIL = 'Email' + __complement


class DoesNotExist(str, Enum):
    __complement = ' does not exist'

    USER = 'User' + __complement


class NotAuthorized(str, Enum):
    __complement = 'Not authorized to '

    REGISTER_EMPLOYEE = __complement + 'register employee'
