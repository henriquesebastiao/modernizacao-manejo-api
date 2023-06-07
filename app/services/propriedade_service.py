from typing import Optional

from sqlalchemy.orm import Session

from app.models.propriedade import Propriedade
from app.repository import BaseRepository
from app.schemas.propriedade import PropriedadeCreateSchema, \
    PropriedadeDeleteSchema, PropriedadeUpdateSchema
from app.services.base_service import BaseService


class PropriedadeService(BaseService):
    def __init__(self, db: Session):
        super().__init__(db, BaseRepository, Propriedade)

    def create_propriedade(self,
                           propriedade: PropriedadeCreateSchema) -> Propriedade:
        """
        Cria um propriedade.

        Args:
            propriedade (PropriedadeCreate): Os dados da propriedade a ser criado.

        Returns:
            Propriedade: O propriedade criado.
        """
        return self.create(propriedade)

    def get_propriedade(self, propriedade_id: int) -> Optional[Propriedade]:
        """
        Retorna uma propriedade com base no seu ID.

        Args:
            propriedade_id (int): O ID do propriedade.

        Returns:
            Optional[Propriedade]: A propriedade encontrado ou None se não for
            encontrado.
        """
        return self.get_by_id(propriedade_id)

    def get_all_propriedades(self) -> list[Propriedade]:
        """
        Retorna uma lista com todos os animais.

        Returns:
            List[Propriedade]: Uma lista com todos os animais.
        """
        return self.get_all()

    def update_propriedade(self, propriedade_id: int,
                           propriedade: PropriedadeUpdateSchema) -> \
            Propriedade:
        """
        Atualiza uma propriedade com base no seu ID.

        Args:
            propriedade_id (int): O ID da propriedade a ser atualizado.
            propriedade (PropriedadeUpdate): Os dados atualizados do propriedade.

        Returns:
            Optional[Propriedade]: A propriedade atualizado ou None se não for
            encontrado.
        """
        propriedade_db = self.get_propriedade(propriedade_id)
        if propriedade:
            propriedade_db = Propriedade(**propriedade.dict())
            return self.update(propriedade_db)
        return Propriedade()

    def delete_propriedade(self, propriedade: PropriedadeDeleteSchema) -> None:
        """
        Remove uma propriedade com base no seu ID.

        Args:
            propriedade (PropriedadeDelete): O ID da propriedade a ser removido.
        """
        propriedade = self.get_propriedade(propriedade.id)
        if propriedade:
            self.delete(propriedade)
