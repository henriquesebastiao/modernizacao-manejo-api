from app.models.fazendeiro import Fazendeiro
from app.schemas.pessoa import PessoaCreate
from app.schemas.user import UserCreate
from app.services.base import BaseService
from app.services.pessoa import PessoaService
from app.services.user import UserService


class FazendeiroService(BaseService):
    def __init__(self):
        super().__init__(Fazendeiro)

    def create(self, entity):
        pessoa = PessoaCreate(nome=entity.nome)
        db_pessoa = PessoaService().create(pessoa)
        user = UserCreate(email=entity.email, password=entity.password,
                          pessoa_id=db_pessoa.id)
        db_user = UserService().create(user)
        self.crud.create(db_user.id)
