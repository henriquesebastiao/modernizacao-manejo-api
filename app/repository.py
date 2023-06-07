from typing import Type, TypeVar

from sqlalchemy.orm import Session

T = TypeVar('T')


class BaseRepository:
    def __init__(self, db: Session, model: Type[T]):
        self.db: Session = db
        self.model: Type[T] = model

    def create(self, entity: T) -> T:
        """
        Cria uma entidade no banco de dados.

        Args:
            entity (T): A entidade a ser criada.

        Returns:
            T: A entidade criada.
        """
        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)
        return entity

    def update(self, entity: T) -> T:
        """
        Atualiza uma entidade no banco de dados.

        Args:
            entity (T): A entidade a ser atualizada.

        Returns:
            T: A entidade atualizada.
        """
        self.db.commit()
        self.db.refresh(entity)
        return entity

    def delete(self, entity: T) -> None:
        """
        Remove uma entidade do banco de dados.

        Args:
            entity (T): A entidade a ser removida.
        """
        self.db.delete(entity)
        self.db.commit()

    def get_all(self) -> list[T]:
        """
        Retorna todas as entidades do tipo T no banco de dados.

        Returns:
            List[T]: Uma lista de entidades do tipo T.
        """
        return self.db.query(self.model).all()

    def get_by_id(self, entity_id: int) -> T:
        """
        Retorna uma lista com uma única entidade do tipo T com base no seu ID.

        Args:
            entity_id (int): O ID da entidade.

        Returns:
            T: Uma entidade encontrada ou None se não for encontrado.
        """
        entity = self.db.query(self.model).filter_by(id=entity_id).first()
        if entity:
            return entity
        return None

    def get_by_field(self, field_name: str, value: str) -> list[T]:
        """
        Retorna uma entidade com base em um campo específico.

        Args:
            field_name (str): O nome do campo a ser usado na busca.
            value (str): O valor a ser buscado no campo.

        Returns:
            Optional[T]: A entidade encontrada ou None se não for encontrada.
        """
        entity = self.db.query(self.model).filter(
            getattr(self.model, field_name) == value).first()
        if entity:
            return [entity]
        return []
