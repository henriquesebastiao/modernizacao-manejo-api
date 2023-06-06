"""Routes for animal"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud.animal import create, delete, get_all, get_by_id, get_by_brinco, update
from app.database import get_db
from app.schemas.animal import AnimalCreate, Animal

router = APIRouter()


@router.post("/animal")
async def create_animal(a: AnimalCreate, db: Session = Depends(get_db)):
    """Cria um animal."""
    return create(a, db)


@router.get("/animal", response_model=list[Animal])
async def get_all_animal(db: Session = Depends(get_db)):
    """Retorna todos os animais."""
    return get_all(db)


@router.get("/animal/{animal_id}")
async def get_animal_by_id(animal_id: int, db: Session = Depends(get_db)):
    """Retorna um animal pelo id."""
    return get_by_id(animal_id, db)


@router.get("/animal/brinco/{brinco}")
async def get_animal_by_id(brinco: str, db: Session = Depends(get_db)):
    """Retorna um animal pelo id."""
    return get_by_brinco(brinco, db)


@router.get("/animal/chip/{chip}")
async def get_animal_by_id(chip: str, db: Session = Depends(get_db)):
    """Retorna um animal pelo id."""
    return get_by_brinco(chip, db)


@router.patch("/animal/{animal_id}")
async def update_animal(animal_id: int, item: AnimalCreate,
                        db: Session = Depends(get_db)):
    """Atualiza um animal."""
    return update(animal_id, item, db)


@router.delete("/animal/{animal_id}")
async def delete_animal(animal_id: int, db: Session = Depends(get_db)):
    """Deleta um animal."""
    return delete(animal_id, db)
