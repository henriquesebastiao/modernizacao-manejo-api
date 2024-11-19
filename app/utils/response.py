from fastapi import status

from app.schemas import raises

CREATE_USER = {
    status.HTTP_409_CONFLICT: {
        'model': raises.EmailAlreadyExists,
    }
}

CREATE_SUBORDINATE_USER = {
    status.HTTP_403_FORBIDDEN: {'model': raises.NotAuthorizedRegisterEmployee},
    status.HTTP_409_CONFLICT: {
        'model': raises.EmailAlreadyExists,
    },
}
