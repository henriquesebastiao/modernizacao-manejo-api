from typing import Optional

from sqlalchemy.orm import Session

from app.models.peso_log import PesoLog
from app.repository import BaseRepository
from app.schemas.peso_log import PesoLogCreateSchema, PesoLogUpdateSchema, \
    PesoLogDeleteSchema
from app.services.base_service import BaseService


class PesoLogService(BaseService):
    def __init__(self, db: Session):
        super().__init__(db, BaseRepository, PesoLog)

    def create_peso_log(self, peso_log: PesoLogCreateSchema) -> PesoLog:
        """
        Cria um peso_log.

        Args:
            peso_log (PesoLogCreate): Os dados do peso_log a ser criado.

        Returns:
            PesoLog: O peso_log criado.
        """
        return self.create(peso_log)

    def get_peso_log(self, peso_log_id: int) -> Optional[PesoLog]:
        """
        Retorna um peso_log com base no seu ID.

        Args:
            peso_log_id (int): O ID do peso_log.

        Returns:
            Optional[PesoLog]: O peso_log encontrado ou None se não for encontrado.
        """
        return self.get_by_id(peso_log_id)

    def get_all_peso_logs(self) -> list[PesoLog]:
        """
        Retorna uma lista com todos os animais.

        Returns:
            List[PesoLog]: Uma lista com todos os animais.
        """
        return self.get_all()

    def update_peso_log(self, peso_log_id: int, peso_log: PesoLogUpdateSchema) -> \
            PesoLog:
        """
        Atualiza um peso_log com base no seu ID.

        Args:
            peso_log_id (int): O ID do peso_log a ser atualizado.
            peso_log (PesoLogUpdate): Os dados atualizados do peso_log.

        Returns:
            Optional[PesoLog]: O peso_log atualizado ou None se não for encontrado.
        """
        peso_log_db = self.get_peso_log(peso_log_id)
        if peso_log:
            peso_log_db = PesoLog(**peso_log.dict())
            return self.update(peso_log_db)
        return PesoLog()

    def delete_peso_log(self, peso_log: PesoLogDeleteSchema) -> None:
        """
        Remove um peso_log com base no seu ID.

        Args:
            peso_log (PesoLogDelete): O ID do peso_log a ser removido.
        """
        peso_log = self.get_peso_log(peso_log.id)
        if peso_log:
            self.delete(peso_log)
