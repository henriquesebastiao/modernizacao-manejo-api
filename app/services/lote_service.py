from typing import Optional

from sqlalchemy.orm import Session

from app.models.lote import Lote
from app.repository import BaseRepository
from app.schemas.lote import LoteCreateSchema, LoteUpdateSchema, \
    LoteDeleteSchema
from app.services.base_service import BaseService


class LoteService(BaseService):
    def __init__(self, db: Session):
        super().__init__(db, BaseRepository, Lote)

    def create_lote(self, lote: LoteCreateSchema) -> Lote:
        """
        Cria um lote.

        Args:
            lote (LoteCreate): Os dados do lote a ser criado.

        Returns:
            Lote: O lote criado.
        """
        return self.create(lote)

    def get_lote(self, lote_id: int) -> Optional[Lote]:
        """
        Retorna um lote com base no seu ID.

        Args:
            lote_id (int): O ID do lote.

        Returns:
            Optional[Lote]: O lote encontrado ou None se não for encontrado.
        """
        return self.get_by_id(lote_id)

    def get_all_lotes(self) -> list[Lote]:
        """
        Retorna uma lista com todos os animais.

        Returns:
            List[Lote]: Uma lista com todos os animais.
        """
        return self.get_all()

    def update_lote(self, lote_id: int, lote: LoteUpdateSchema) -> \
            Lote:
        """
        Atualiza um lote com base no seu ID.

        Args:
            lote_id (int): O ID do lote a ser atualizado.
            lote (LoteUpdate): Os dados atualizados do lote.

        Returns:
            Optional[Lote]: O lote atualizado ou None se não for encontrado.
        """
        lote_db = self.get_lote(lote_id)
        if lote:
            lote_db = Lote(**lote.dict())
            return self.update(lote_db)
        return Lote()

    def delete_lote(self, lote: LoteDeleteSchema) -> None:
        """
        Remove um lote com base no seu ID.

        Args:
            lote (LoteDelete): O ID do lote a ser removido.
        """
        lote = self.get_lote(lote.id)
        if lote:
            self.delete(lote)
