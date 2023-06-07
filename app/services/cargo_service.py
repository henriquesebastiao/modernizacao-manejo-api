from typing import Optional

from sqlalchemy.orm import Session

from app.models.cargo import Cargo
from app.repository import BaseRepository
from app.schemas.cargo import CargoCreateSchema, CargoUpdateSchema, \
    CargoDeleteSchema
from app.services.base_service import BaseService


class CargoService(BaseService):
    def __init__(self, db: Session):
        super().__init__(db, BaseRepository, Cargo)

    def create_cargo(self, cargo: CargoCreateSchema) -> Cargo:
        """
        Cria um cargo.

        Args:
            cargo (CargoCreate): Os dados do cargo a ser criado.

        Returns:
            Cargo: O cargo criado.
        """
        return self.create(cargo)

    def get_cargo(self, cargo_id: int) -> Optional[Cargo]:
        """
        Retorna um cargo com base no seu ID.

        Args:
            cargo_id (int): O ID do cargo.

        Returns:
            Optional[Cargo]: O cargo encontrado ou None se não for encontrado.
        """
        return self.get_by_id(cargo_id)

    def get_all_cargos(self) -> list[Cargo]:
        """
        Retorna uma lista com todos os animais.

        Returns:
            List[Cargo]: Uma lista com todos os animais.
        """
        return self.get_all()

    def update_cargo(self, cargo_id: int, cargo: CargoUpdateSchema) -> \
            Cargo:
        """
        Atualiza um cargo com base no seu ID.

        Args:
            cargo_id (int): O ID do cargo a ser atualizado.
            cargo (CargoUpdate): Os dados atualizados do cargo.

        Returns:
            Optional[Cargo]: O cargo atualizado ou None se não for encontrado.
        """
        cargo_db = self.get_cargo(cargo_id)
        if cargo:
            cargo_db = Cargo(**cargo.dict())
            return self.update(cargo_db)
        return Cargo()

    def delete_cargo(self, cargo: CargoDeleteSchema) -> None:
        """
        Remove um cargo com base no seu ID.

        Args:
            cargo (CargoDelete): O ID do cargo a ser removido.
        """
        cargo = self.get_cargo(cargo.id)
        if cargo:
            self.delete(cargo)
