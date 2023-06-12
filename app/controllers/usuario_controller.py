from typing import Type, TypeVar

from sqlalchemy.orm import Session

from app.controllers.base_controller import BaseControllers
from app.repositories.repository import BaseRepository
from app.schemas.usuario import UsuarioLoginSchema

T = TypeVar('T')


class UsuarioController(BaseControllers):
    def __init__(self, db: Session, model: Type[T] = None):
        super().__init__(db, model)

    def login(self, usuario: UsuarioLoginSchema) -> bool:
        """
        Cria um animal.

        Args:
            usuario (UsuarioLoginSchema): Os dados do animal a ser criado.

        Returns:
            Animal: O animal criado.
        """
        try:
            usuario_db = BaseRepository(self.db, self.model).get_by_field(
                "email", usuario.email)
            if usuario_db is None:
                raise Exception
            if usuario_db[0].password != usuario.password:
                raise Exception
        except Exception:
            return False
        return True
