from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.controllers.animal_controller import AnimalController
from app.database import get_db
from app.models.animal import Animal
from app.schemas.animal import AnimalCreateSchema, AnimalSchema, \
    AnimalUpdateSchema

router = APIRouter(prefix="/animal", tags=["Animal"])


@router.post("/", status_code=201)
async def create(animal: AnimalCreateSchema,
                 db: Session = Depends(get_db)):
    controller = AnimalController(db, Animal)
    if controller.create(animal):
        return "Criado com sucesso"
    raise HTTPException(status_code=404, detail="Nenhum registro criado")


@router.get("/{animal_id}", response_model=AnimalSchema)
def get_by_id(animal_id: int, db: Session = Depends(get_db)):
    controller = AnimalController(db, Animal)
    if db_animal := controller.get_by_id(animal_id):
        return db_animal
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.get("/{brinco}", response_model=AnimalSchema)
def get_by_brinco(brinco: str, db: Session = Depends(get_db)):
    controller = AnimalController(db, Animal)
    if db_animal := controller.get_by_field(brinco, brinco):
        return db_animal
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.get("/{chip}", response_model=AnimalSchema)
def get_by_chip(chip: str, db: Session = Depends(get_db)):
    controller = AnimalController(db, Animal)
    if db_animal := controller.get_by_field(chip, chip):
        return db_animal
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.get("/", response_model=list[AnimalSchema])
async def get_all(db: Session = Depends(get_db)):
    controller = AnimalController(db, Animal)
    if db_animal := controller.get_all():
        return db_animal
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.patch("/{animal_id}")
async def update(animal_id: int, animal: AnimalUpdateSchema,
                 db: Session = Depends(get_db)):
    controller = AnimalController(db, Animal)
    if controller.update(animal_id, animal):
        return {"mensagem": "Atualizado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.delete("/{animal_id}")
async def delete(animal_id: int, db: Session = Depends(get_db)) -> dict:
    controller = AnimalController(db, Animal)
    if controller.delete(animal_id):
        return {"message": "Apagado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")
