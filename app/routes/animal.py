"""Routes for animal"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.animal import AnimalCreateSchema, AnimalSchema, \
    AnimalUpdateSchema, AnimalDeleteSchema
from app.services.animal_service import AnimalService

router = APIRouter(prefix="/animals", tags=["Animals"])


@router.post("/", response_model=AnimalSchema)
async def create_animal(animal: AnimalCreateSchema,
                        db: Session = Depends(get_db)):
    """Cria um animal."""
    animal_service = AnimalService(db)
    return animal_service.create_animal(animal)


@router.get("/{animal_id}", response_model=AnimalSchema)
def get_animal(animal_id: int, db: Session = Depends(get_db)):
    """Retorna um animal com base no seu ID."""
    animal_service = AnimalService(db)
    return animal_service.get_animal(animal_id)


@router.get("/{brinco}", response_model=AnimalSchema)
def get_animal(brinco: str, db: Session = Depends(get_db)):
    """Retorna um animal com base no seu ID."""
    animal_service = AnimalService(db)
    return animal_service.get_by_field(brinco, brinco)


@router.get("/{animal_id}", response_model=AnimalSchema)
def get_animal(chip: str, db: Session = Depends(get_db)):
    """Retorna um animal com base no seu ID."""
    animal_service = AnimalService(db)
    return animal_service.get_by_field(chip, chip)


@router.get("/")
async def get_all_animals(db: Session = Depends(get_db)):
    """Retorna todos os animais."""
    animal_service = AnimalService(db)
    return animal_service.get_all_animals()


@router.patch("/animal/{animal_id}")
async def update_animal(animal_id: int, animal: AnimalUpdateSchema,
                        db: Session = Depends(get_db)):
    """Atualiza um animal."""
    animal_service = AnimalService(db)
    return animal_service.update_animal(animal_id, animal)


@router.delete("/animal/{animal_id}")
async def delete_animal(animal: AnimalDeleteSchema, db: Session = Depends(get_db)):
    """Deleta um animal."""
    animal_service = AnimalService(db)
    animal_service.delete_animal(animal)
    return {"message": "Animal deleted"}
