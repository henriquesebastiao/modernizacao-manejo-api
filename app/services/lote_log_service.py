from typing import Optional

from sqlalchemy.orm import Session

from app.models.lote_log import LoteLog
from app.repository import BaseRepository
from app.schemas.lote_log import LoteLogCreateSchema, LoteLogUpdateSchema, \
    LoteLogDeleteSchema
from app.services.base_service import BaseService


class LoteLogService(BaseService):
    def __init__(self, db: Session):
        super().__init__(db, BaseRepository, LoteLog)

    def create_lote_log(self, lote_log: LoteLogCreateSchema) -> LoteLog:
        """
        Cria um lote_log.

        Args:
            lote_log (LoteLogCreate): Os dados do lote_log a ser criado.

        Returns:
            LoteLog: O lote_log criado.
        """
        return self.create(lote_log)

    def get_lote_log(self, lote_log_id: int) -> Optional[LoteLog]:
        """
        Retorna um lote_log com base no seu ID.

        Args:
            lote_log_id (int): O ID do lote_log.

        Returns:
            Optional[LoteLog]: O lote_log encontrado ou None se não for encontrado.
        """
        return self.get_by_id(lote_log_id)

    def get_all_lote_logs(self) -> list[LoteLog]:
        """
        Retorna uma lista com todos os animais.

        Returns:
            List[LoteLog]: Uma lista com todos os animais.
        """
        return self.get_all()

    def update_lote_log(self, lote_log_id: int, lote_log: LoteLogUpdateSchema) -> \
            LoteLog:
        """
        Atualiza um lote_log com base no seu ID.

        Args:
            lote_log_id (int): O ID do lote_log a ser atualizado.
            lote_log (LoteLogUpdate): Os dados atualizados do lote_log.

        Returns:
            Optional[LoteLog]: O lote_log atualizado ou None se não for encontrado.
        """
        lote_log_db = self.get_lote_log(lote_log_id)
        if lote_log:
            lote_log_db = LoteLog(**lote_log.dict())
            return self.update(lote_log_db)
        return LoteLog()

    def delete_lote_log(self, lote_log: LoteLogDeleteSchema) -> None:
        """
        Remove um lote_log com base no seu ID.

        Args:
            lote_log (LoteLogDelete): O ID do lote_log a ser removido.
        """
        lote_log = self.get_lote_log(lote_log.id)
        if lote_log:
            self.delete(lote_log)
