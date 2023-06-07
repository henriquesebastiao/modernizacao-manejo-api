from typing import Optional

from sqlalchemy.orm import Session

from app.models.fazenda import Fazenda
from app.repository import BaseRepository
from app.schemas.fazenda import FazendaCreateSchema, FazendaUpdateSchema, \
    FazendaDeleteSchema
from app.services.base_service import BaseService


class FazendaService(BaseService):
    def __init__(self, db: Session):
        super().__init__(db, BaseRepository, Fazenda)

    def create_fazenda(self, fazenda: FazendaCreateSchema) -> Fazenda:
        """
        Cria um fazenda.

        Args:
            fazenda (FazendaCreate): Os dados do fazenda a ser criado.

        Returns:
            Fazenda: O fazenda criado.
        """
        return self.create(fazenda)

    def get_fazenda(self, fazenda_id: int) -> Optional[Fazenda]:
        """
        Retorna um fazenda com base no seu ID.

        Args:
            fazenda_id (int): O ID do fazenda.

        Returns:
            Optional[Fazenda]: O fazenda encontrado ou None se não for encontrado.
        """
        return self.get_by_id(fazenda_id)

    def get_all_fazendas(self) -> list[Fazenda]:
        """
        Retorna uma lista com todos os animais.

        Returns:
            List[Fazenda]: Uma lista com todos os animais.
        """
        return self.get_all()

    def update_fazenda(self, fazenda_id: int, fazenda: FazendaUpdateSchema) -> \
            Fazenda:
        """
        Atualiza um fazenda com base no seu ID.

        Args:
            fazenda_id (int): O ID do fazenda a ser atualizado.
            fazenda (FazendaUpdate): Os dados atualizados do fazenda.

        Returns:
            Optional[Fazenda]: O fazenda atualizado ou None se não for encontrado.
        """
        fazenda_db = self.get_fazenda(fazenda_id)
        if fazenda:
            fazenda_db = Fazenda(**fazenda.dict())
            return self.update(fazenda_db)
        return Fazenda()

    def delete_fazenda(self, fazenda: FazendaDeleteSchema) -> None:
        """
        Remove um fazenda com base no seu ID.

        Args:
            fazenda (FazendaDelete): O ID do fazenda a ser removido.
        """
        fazenda = self.get_fazenda(fazenda.id)
        if fazenda:
            self.delete(fazenda)
