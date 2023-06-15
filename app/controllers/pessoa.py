from app.controllers.base import BaseControllers

from app.models.pessoa import Pessoa


class PessoaController(BaseControllers):
    def __init__(self):
        super().__init__(Pessoa)
