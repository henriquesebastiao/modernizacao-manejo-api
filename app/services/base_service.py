from typing import Type, TypeVar, Optional

from pydantic import BaseModel

from sqlalchemy.orm import Session

T = TypeVar('T')


class BaseService:
    def __init__(self, db: Session, repository: Type[T], model: Type[T] = None):
        self.db: Session = db
        self.repository: Type[T] = repository
        self.model: Type[T] = model

    def create(self, entity: BaseModel) -> T:
        """
        Cria uma entidade.

        Args:
            entity (T): A entidade a ser criada.

        Returns:
            T: A entidade criada.
        """
        entity = self.model(**entity.dict())
        return self.repository(self.db, self.model).create(entity)

    def update(self, entity: BaseModel) -> T:
        """
        Atualiza uma entidade.

        Args:
            entity (T): A entidade a ser atualizada.

        Returns:
            T: A entidade atualizada.
        """
        return self.repository(self.db, self.model).update(entity)

    def delete(self, entity: BaseModel) -> None:
        """
        Remove uma entidade.

        Args:
            entity (T): A entidade a ser removida.
        """
        self.repository(self.db, self.model).delete(entity)

    def get_all(self) -> list[T]:
        """
        Retorna todas as entidades.

        Returns:
            List[T]: Uma lista de entidades.
        """
        return self.repository(self.db, self.model).get_all()

    def get_by_id(self, entity_id: int) -> T:
        """
        Retorna uma entidade com base no seu ID.

        Args:
            entity_id (int): O ID da entidade.

        Returns:
            Optional[T]: A entidade encontrada ou None se não for encontrada.
        """
        return self.repository(self.db, self.model).get_by_id(entity_id)

    def get_by_field(self, field_name: str, value: str) -> list[T]:
        """
        Retorna uma entidade com base em um campo específico.

        Args:
            field_name (str): O nome do campo a ser usado na busca.
            value (str): O valor a ser buscado no campo.

        Returns:
            List[T]: Uma lista contendo a entidade encontrada ou uma lista vazia
             se não for encontrada.
        """
        return self.repository(self.db).get_by_field(field_name, value)
