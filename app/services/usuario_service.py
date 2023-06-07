from typing import Optional

from sqlalchemy.orm import Session

from app.models.usuario import Usuario
from app.repository import BaseRepository
from app.schemas.usuario import UsuarioCreateSchema, UsuarioUpdateSchema, \
    UsuarioDeleteSchema
from app.services.base_service import BaseService


class UsuarioService(BaseService):
    def __init__(self, db: Session):
        super().__init__(db, BaseRepository, Usuario)

    def create_usuario(self, usuario: UsuarioCreateSchema) -> Usuario:
        """
        Cria um usuario.

        Args:
            usuario (UsuarioCreate): Os dados do usuario a ser criado.

        Returns:
            Usuario: O usuario criado.
        """
        return self.create(usuario)

    def get_usuario(self, usuario_id: int) -> Optional[Usuario]:
        """
        Retorna um usuario com base no seu ID.

        Args:
            usuario_id (int): O ID do usuario.

        Returns:
            Optional[Usuario]: O usuario encontrado ou None se não for encontrado.
        """
        return self.get_by_id(usuario_id)

    def get_all_usuarios(self) -> list[Usuario]:
        """
        Retorna uma lista com todos os animais.

        Returns:
            List[Usuario]: Uma lista com todos os animais.
        """
        return self.get_all()

    def update_usuario(self, usuario_id: int, usuario: UsuarioUpdateSchema) -> \
            Usuario:
        """
        Atualiza um usuario com base no seu ID.

        Args:
            usuario_id (int): O ID do usuario a ser atualizado.
            usuario (UsuarioUpdate): Os dados atualizados do usuario.

        Returns:
            Optional[Usuario]: O usuario atualizado ou None se não for encontrado.
        """
        usuario_db = self.get_usuario(usuario_id)
        if usuario:
            usuario_db = Usuario(**usuario.dict())
            return self.update(usuario_db)
        return Usuario()

    def delete_usuario(self, usuario: UsuarioDeleteSchema) -> None:
        """
        Remove um usuario com base no seu ID.

        Args:
            usuario (UsuarioDelete): O ID do usuario a ser removido.
        """
        usuario = self.get_usuario(usuario.id)
        if usuario:
            self.delete(usuario)
