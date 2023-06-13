from sqlalchemy.orm import Session

from app.models.base import Base


class BaseRepository:
    def __init__(self, db: Session, model: Base):
        self.db: Session = db
        self.model: Base = model

    def create(self, entity: Base) -> bool:
        """
        Cria uma entidade no banco de dados.

        Args:
            entity (T): A entidade a ser criada.

        Returns:
            T: A entidade criada.
        """
        try:
            self.db.add(entity)
            self.db.commit()
            self.db.refresh(entity)
        except Exception:
            self.db.rollback()
            raise Exception
        return True

    def update(self, entity: Base) -> bool:
        """
        Atualiza uma entidade no banco de dados.

        Args:
            entity (T): A entidade a ser atualizada.

        Returns:
            T: A entidade atualizada.
        """
        try:
            self.db.commit()
            self.db.refresh(entity)
        except Exception:
            self.db.rollback()
            raise Exception
        return True

    def delete(self, entity: Base) -> bool:
        """
        Remove uma entidade do banco de dados.

        Args:
            entity (T): A entidade a ser removida.
        """
        try:
            self.db.delete(entity)
            self.db.commit()
        except Exception:
            self.db.rollback()
            raise Exception
        return True

    def get_all(self) -> list[Base]:
        """
        Retorna todas as entidades do tipo T no banco de dados.

        Returns:
            Optional[T]: A entidade encontrada ou None se não for encontrada.
        """
        try:
            entity = self.db.query(self.model).all()
        except Exception:
            raise Exception
        return entity

    def get_by_id(self, entity_id: int) -> Base:
        """
        Retorna uma lista com uma única entidade do tipo T com base no seu ID.

        Args:
            entity_id (int): O ID da entidade.

        Returns:
            T: Uma entidade encontrada ou None se não for encontrado.
        """
        try:
            entity = self.db.query(self.model).filter_by(id=entity_id).first()
            if not entity:
                raise Exception
        except Exception:
            raise Exception
        return entity

    def get_by_field(self, field_name: str, value: str) -> list[Base]:
        """
        Retorna uma entidade com base em um campo específico.

        Args:
            field_name (str): O nome do campo a ser usado na busca.
            value (str): O valor a ser buscado no campo.

        Returns:
            Optional[T]: A entidade encontrada ou None se não for encontrada.
        """
        try:
            entity = self.db.query(self.model).filter(
                getattr(self.model, field_name) == value).all()
            if not entity:
                raise Exception
        except Exception:
            raise Exception
        return entity
