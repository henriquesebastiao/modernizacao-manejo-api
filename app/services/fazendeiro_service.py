from typing import Optional

from sqlalchemy.orm import Session

from app.models.fazendeiro import Fazendeiro
from app.repository import BaseRepository
from app.schemas.fazendeiro import FazendeiroCreateSchema, \
    FazendeiroDeleteSchema, FazendeiroUpdateSchema
from app.services.base_service import BaseService


class FazendeiroService(BaseService):
    def __init__(self, db: Session):
        super().__init__(db, BaseRepository, Fazendeiro)

    def create_fazendeiro(self,
                          fazendeiro: FazendeiroCreateSchema) -> Fazendeiro:
        """
        Cria um fazendeiro.

        Args:
            fazendeiro (FazendeiroCreate): Os dados do fazendeiro a ser criado.

        Returns:
            Fazendeiro: O fazendeiro criado.
        """
        return self.create(fazendeiro)

    def get_fazendeiro(self, fazendeiro_id: int) -> Optional[Fazendeiro]:
        """
        Retorna um fazendeiro com base no seu ID.

        Args:
            fazendeiro_id (int): O ID do fazendeiro.

        Returns:
            Optional[Fazendeiro]: O fazendeiro encontrado ou None se não for encontrado.
        """
        return self.get_by_id(fazendeiro_id)

    def get_all_fazendeiros(self) -> list[Fazendeiro]:
        """
        Retorna uma lista com todos os animais.

        Returns:
            List[Fazendeiro]: Uma lista com todos os animais.
        """
        return self.get_all()

    def update_fazendeiro(self, fazendeiro_id: int,
                          fazendeiro: FazendeiroUpdateSchema) -> \
            Fazendeiro:
        """
        Atualiza um fazendeiro com base no seu ID.

        Args:
            fazendeiro_id (int): O ID do fazendeiro a ser atualizado.
            fazendeiro (FazendeiroUpdate): Os dados atualizados do fazendeiro.

        Returns:
            Optional[Fazendeiro]: O fazendeiro atualizado ou None se não for encontrado.
        """
        fazendeiro_db = self.get_fazendeiro(fazendeiro_id)
        if fazendeiro:
            fazendeiro_db = Fazendeiro(**fazendeiro.dict())
            return self.update(fazendeiro_db)
        return Fazendeiro()

    def delete_fazendeiro(self, fazendeiro: FazendeiroDeleteSchema) -> None:
        """
        Remove um fazendeiro com base no seu ID.

        Args:
            fazendeiro (FazendeiroDelete): O ID do fazendeiro a ser removido.
        """
        fazendeiro = self.get_fazendeiro(fazendeiro.id)
        if fazendeiro:
            self.delete(fazendeiro)
