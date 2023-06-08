from typing import Type, TypeVar

from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.repository import BaseRepository

T = TypeVar('T')


class BaseService:
    def __init__(self, db: Session, model: Type[T] = None):
        self.db: Session = db
        self.model: Type[T] = model

    def create(self, entity: BaseModel) -> T | None:
        """
        Cria uma entidade.

        Args:
            entity (T): A entidade a ser criada.

        Returns:
            T: A entidade criada.
        """
        entity = self.model(**entity.dict())
        return BaseRepository(self.db, self.model).create(entity)

    def update(self, entity_id: int, entity: BaseModel) -> T | None:
        """
        Atualiza uma entidade.

        Args:
            entity_id (int): O ID da entidade a ser atualizada.
            entity (T): A entidade a ser atualizada.

        Returns:
            T: A entidade atualizada.
        """
        db_entity = self.get_by_id(entity_id)
        if db_entity:
            for field, value in entity.dict(exclude_unset=True).items():
                setattr(db_entity, field, value)
            return BaseRepository(self.db, self.model).update(db_entity)
        return None

    def delete(self, entity_id: int) -> T | None:
        """
        Remove uma entidade.

        Args:
            entity_id: A entidade a ser removida.
        """
        entity = self.get_by_id(entity_id)
        if entity:
            return BaseRepository(self.db, self.model).delete(entity)
        return None

    def get_all(self) -> list[T] | None:
        """
        Retorna todas as entidades.

        Returns:
            List[T]: Uma lista de entidades.
        """
        return BaseRepository(self.db, self.model).get_all()

    def get_by_id(self, entity_id: int) -> T | None:
        """
        Retorna uma entidade com base no seu ID.

        Args:
            entity_id (int): O ID da entidade.

        Returns:
            Optional[T]: A entidade encontrada ou None se não for encontrada.
        """
        return BaseRepository(self.db, self.model).get_by_id(entity_id)

    def get_by_field(self, field_name: str, value: str) -> list[T] | None:
        """
        Retorna uma entidade com base em um campo específico.

        Args:
            field_name (str): O nome do campo a ser usado na busca.
            value (str): O valor a ser buscado no campo.

        Returns:
            List[T]: Uma lista contendo a entidade encontrada ou uma lista vazia
             se não for encontrada.
        """
        return BaseRepository(self.db, self.model).get_by_field(field_name,
                                                                value)
