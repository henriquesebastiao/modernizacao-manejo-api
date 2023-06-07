from typing import Optional

from sqlalchemy.orm import Session

from app.models.animal import Animal
from app.repository import BaseRepository
from app.schemas.animal import AnimalCreateSchema, AnimalUpdateSchema, \
    AnimalDeleteSchema
from app.services.base_service import BaseService


class AnimalService(BaseService):
    def __init__(self, db: Session):
        super().__init__(db, BaseRepository, Animal)

    def create_animal(self, animal: AnimalCreateSchema) -> Animal:
        """
        Cria um animal.

        Args:
            animal (AnimalCreate): Os dados do animal a ser criado.

        Returns:
            Animal: O animal criado.
        """
        return self.create(animal)

    def get_animal(self, animal_id: int) -> Optional[Animal]:
        """
        Retorna um animal com base no seu ID.

        Args:
            animal_id (int): O ID do animal.

        Returns:
            Optional[Animal]: O animal encontrado ou None se não for encontrado.
        """
        return self.get_by_id(animal_id)

    def get_all_animals(self) -> list[Animal]:
        """
        Retorna uma lista com todos os animais.

        Returns:
            List[Animal]: Uma lista com todos os animais.
        """
        return self.get_all()

    def update_animal(self, animal_id: int, animal: AnimalUpdateSchema) -> \
            Animal:
        """
        Atualiza um animal com base no seu ID.

        Args:
            animal_id (int): O ID do animal a ser atualizado.
            animal (AnimalUpdate): Os dados atualizados do animal.

        Returns:
            Optional[Animal]: O animal atualizado ou None se não for encontrado.
        """
        animal_db = self.get_animal(animal_id)
        if animal:
            animal_db = Animal(**animal.dict())
            return self.update(animal_db)
        return Animal()

    def delete_animal(self, animal: AnimalDeleteSchema) -> None:
        """
        Remove um animal com base no seu ID.

        Args:
            animal (AnimalDelete): O ID do animal a ser removido.
        """
        animal = self.get_animal(animal.id)
        if animal:
            self.delete(animal)
