from app.services.base import BaseService
from app.services.pessoa import PessoaService
from app.services.user import UserService

from app.models.fazendeiro import Fazendeiro

from app.schemas.user import UserCreate
from app.schemas.pessoa import PessoaCreate


class FazendeiroService(BaseService):
    def __init__(self):
        super().__init__(Fazendeiro)

    def create(self, entity):
        user = UserCreate(email=entity.email, password=entity.password)
        db_user = UserService().create(user)
        pessoa = PessoaCreate(nome=entity.nome, user_id=db_user.id)
        db_pessoa = PessoaService().create(pessoa)
        self.create(db_pessoa.id)
