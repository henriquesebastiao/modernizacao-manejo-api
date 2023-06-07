from typing import Optional

from sqlalchemy.orm import Session

from app.models.pessoa import Pessoa
from app.repository import BaseRepository
from app.schemas.pessoa import PessoaCreateSchema, PessoaUpdateSchema, \
    PessoaDeleteSchema
from app.services.base_service import BaseService


class PessoaService(BaseService):
    def __init__(self, db: Session):
        super().__init__(db, BaseRepository, Pessoa)

    def create_pessoa(self, pessoa: PessoaCreateSchema) -> Pessoa:
        """
        Cria um pessoa.

        Args:
            pessoa (PessoaCreate): Os dados da pessoa a ser criado.

        Returns:
            Pessoa: O pessoa criado.
        """
        return self.create(pessoa)

    def get_pessoa(self, pessoa_id: int) -> Optional[Pessoa]:
        """
        Retorna uma pessoa com base no seu ID.

        Args:
            pessoa_id (int): O ID do pessoa.

        Returns:
            Optional[Pessoa]: O pessoa encontrado ou None se não for encontrado.
        """
        return self.get_by_id(pessoa_id)

    def get_all_pessoas(self) -> list[Pessoa]:
        """
        Retorna uma lista com todos os animais.

        Returns:
            List[Pessoa]: Uma lista com todos os animais.
        """
        return self.get_all()

    def update_pessoa(self, pessoa_id: int, pessoa: PessoaUpdateSchema) -> \
            Pessoa:
        """
        Atualiza uma pessoa com base no seu ID.

        Args:
            pessoa_id (int): O ID da pessoa a ser atualizado.
            pessoa (PessoaUpdate): Os dados atualizados do pessoa.

        Returns:
            Optional[Pessoa]: O pessoa atualizado ou None se não for encontrado.
        """
        pessoa_db = self.get_pessoa(pessoa_id)
        if pessoa:
            pessoa_db = Pessoa(**pessoa.dict())
            return self.update(pessoa_db)
        return Pessoa()

    def delete_pessoa(self, pessoa: PessoaDeleteSchema) -> None:
        """
        Remove uma pessoa com base no seu ID.

        Args:
            pessoa (PessoaDelete): O ID da pessoa a ser removido.
        """
        pessoa = self.get_pessoa(pessoa.id)
        if pessoa:
            self.delete(pessoa)
