from fastapi import APIRouter

from crud import animal
from schemas.animal import AnimalCreate

router = APIRouter()


@router.post("/animal")
async def create_animal(an: AnimalCreate):
    return animal.create(an)


@router.get("/animal")
async def get_all_animal():
    return animal.get_all()


@router.get("/animal/{animal_id}")
async def get_animal_by_id(animal_id: int):
    return animal.get_byid(animal_id)


@router.patch("/animal/{animal_id}")
async def update_animal(animal_id: int, create: AnimalCreate):
    return animal.update(animal_id, create)


@router.delete("/animal/{animal_id}")
async def delete_animal(animal_id: int):
    return animal.delete(animal_id)
