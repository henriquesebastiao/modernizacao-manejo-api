"""Routes for animal"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud import animal
from app.database import get_db
from app.schemas.animal import AnimalCreate

router = APIRouter()


@router.post("/animal")
async def create_animal(item: AnimalCreate, db: Session = Depends(get_db)):
    """Cria um animal."""
    return animal.create(item, db)


@router.get("/animal")
async def get_all_animal(db: Session = Depends(get_db)):
    """Retorna todos os animais."""
    return animal.get_all(db)


@router.get("/animal/{animal_id}")
async def get_animal_by_id(animal_id: int, db: Session = Depends(get_db)):
    """Retorna um animal pelo id."""
    return animal.get_byid(animal_id, db)


@router.patch("/animal/{animal_id}")
async def update_animal(animal_id: int, item: AnimalCreate,
                        db: Session = Depends(get_db)):
    """Atualiza um animal."""
    return animal.update(animal_id, item, db)


@router.delete("/animal/{animal_id}")
async def delete_animal(animal_id: int, db: Session = Depends(get_db)):
    """Deleta um animal."""
    return animal.delete(animal_id, db)
