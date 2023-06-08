"""Routes for animal"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.animal import Animal
from app.schemas.animal import AnimalCreateSchema, AnimalUpdateSchema
from app.services.animal_service import AnimalService

router = APIRouter(prefix="/animal", tags=["Animal"])


@router.post("/")
async def create_animal(animal: AnimalCreateSchema,
                        db: Session = Depends(get_db)):
    """Cria um animal."""
    service = AnimalService(db, Animal)
    if service.create(animal):
        return {"mensagem": "Criado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.get("/{animal_id}")
def get_animal_by_id(animal_id: int, db: Session = Depends(get_db)):
    """Retorna um animal com base no seu ID."""
    service = AnimalService(db, Animal)
    if db_animal := service.get_by_id(animal_id):
        return db_animal
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.get("/{brinco}")
def get_animal_by_brinco(brinco: str, db: Session = Depends(get_db)):
    """Retorna um animal com base no seu ID."""
    service = AnimalService(db, Animal)
    if db_animal := service.get_by_field(brinco, brinco):
        return db_animal
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.get("/{chip}")
def get_animal_by_chip(chip: str, db: Session = Depends(get_db)):
    """Retorna um animal com base no seu ID."""
    service = AnimalService(db, Animal)
    if db_animal := service.get_by_field(chip, chip):
        return db_animal
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.get("/")
async def get_all_animals(db: Session = Depends(get_db)):
    """Retorna todos os animais."""
    service = AnimalService(db, Animal)
    if db_animal := service.get_all():
        return db_animal
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.patch("/animal/{animal_id}")
async def update_animal(animal_id: int, animal: AnimalUpdateSchema,
                        db: Session = Depends(get_db)):
    """Atualiza um animal."""
    service = AnimalService(db, Animal)
    if service.update(animal_id, animal):
        return {"mensagem": "Atualizado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.delete("/animal/{animal_id}")
async def delete_animal(animal_id: int, db: Session = Depends(get_db)) -> dict:
    """Deleta um animal."""
    service = AnimalService(db, Animal)
    if service.delete(animal_id):
        return {"message": "Apagado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")
