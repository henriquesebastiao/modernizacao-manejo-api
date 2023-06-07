from typing import Optional

from sqlalchemy.orm import Session

from app.models.raca import Raca
from app.repository import BaseRepository
from app.schemas.raca import RacaCreateSchema, RacaUpdateSchema, \
    RacaDeleteSchema
from app.services.base_service import BaseService


class RacaService(BaseService):
    def __init__(self, db: Session):
        super().__init__(db, BaseRepository, Raca)

    def create_raca(self, raca: RacaCreateSchema) -> Raca:
        """
        Cria um raca.

        Args:
            raca (RacaCreate): Os dados do raca a ser criado.

        Returns:
            Raca: O raca criado.
        """
        return self.create(raca)

    def get_raca(self, raca_id: int) -> Optional[Raca]:
        """
        Retorna um raca com base no seu ID.

        Args:
            raca_id (int): O ID do raca.

        Returns:
            Optional[Raca]: O raca encontrado ou None se não for encontrado.
        """
        return self.get_by_id(raca_id)

    def get_all_racas(self) -> list[Raca]:
        """
        Retorna uma lista com todos os animais.

        Returns:
            List[Raca]: Uma lista com todos os animais.
        """
        return self.get_all()

    def update_raca(self, raca_id: int, raca: RacaUpdateSchema) -> \
            Raca:
        """
        Atualiza um raca com base no seu ID.

        Args:
            raca_id (int): O ID do raca a ser atualizado.
            raca (RacaUpdate): Os dados atualizados do raca.

        Returns:
            Optional[Raca]: O raca atualizado ou None se não for encontrado.
        """
        raca_db = self.get_raca(raca_id)
        if raca:
            raca_db = Raca(**raca.dict())
            return self.update(raca_db)
        return Raca()

    def delete_raca(self, raca: RacaDeleteSchema) -> None:
        """
        Remove um raca com base no seu ID.

        Args:
            raca (RacaDelete): O ID do raca a ser removido.
        """
        raca = self.get_raca(raca.id)
        if raca:
            self.delete(raca)
