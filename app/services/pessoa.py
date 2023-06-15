from app.services.base import BaseService

from app.models.pessoa import Pessoa


class PessoaService(BaseService):
    def __init__(self):
        super().__init__(Pessoa)
