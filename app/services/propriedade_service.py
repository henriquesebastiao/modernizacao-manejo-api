from typing import Optional

from sqlalchemy.orm import Session

from app.models.propriedade import Propriedade
from app.repository import BaseRepository
from app.schemas.propriedade import PropriedadeCreateSchema, PropriedadeUpdateSchema, \
    PropriedadeDeleteSchema
from app.services.base_service import BaseService


class PropriedadeService(BaseService):
    def __init__(self, db: Session):
        super().__init__(db, BaseRepository, Propriedade)

    def create_propriedade(self, propriedade: PropriedadeCreateSchema) -> Propriedade:
        """
        Cria um propriedade.

        Args:
            propriedade (PropriedadeCreate): Os dados do propriedade a ser criado.

        Returns:
            Propriedade: O propriedade criado.
        """
        return self.create(propriedade)

    def get_propriedade(self, propriedade_id: int) -> Optional[Propriedade]:
        """
        Retorna um propriedade com base no seu ID.

        Args:
            propriedade_id (int): O ID do propriedade.

        Returns:
            Optional[Propriedade]: O propriedade encontrado ou None se não for encontrado.
        """
        return self.get_by_id(propriedade_id)

    def get_all_propriedades(self) -> list[Propriedade]:
        """
        Retorna uma lista com todos os animais.

        Returns:
            List[Propriedade]: Uma lista com todos os animais.
        """
        return self.get_all()

    def update_propriedade(self, propriedade_id: int, propriedade: PropriedadeUpdateSchema) -> \
            Propriedade:
        """
        Atualiza um propriedade com base no seu ID.

        Args:
            propriedade_id (int): O ID do propriedade a ser atualizado.
            propriedade (PropriedadeUpdate): Os dados atualizados do propriedade.

        Returns:
            Optional[Propriedade]: O propriedade atualizado ou None se não for encontrado.
        """
        propriedade_db = self.get_propriedade(propriedade_id)
        if propriedade:
            propriedade_db = Propriedade(**propriedade.dict())
            return self.update(propriedade_db)
        return Propriedade()

    def delete_propriedade(self, propriedade: PropriedadeDeleteSchema) -> None:
        """
        Remove um propriedade com base no seu ID.

        Args:
            propriedade (PropriedadeDelete): O ID do propriedade a ser removido.
        """
        propriedade = self.get_propriedade(propriedade.id)
        if propriedade:
            self.delete(propriedade)
