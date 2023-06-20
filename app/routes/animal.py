from fastapi import APIRouter, Depends

from app.database import get_session
from app.schemas.animal import AnimalCreate, AnimalSchema, AnimalUpdate
from app.services.animal import AnimalService

router = APIRouter(prefix="/animal", tags=["Animal"])


@router.post("/")
async def create(cargo: AnimalCreate, session=Depends(get_session)):
    service = AnimalService(session)
    return await service.create(cargo)


@router.get("/{animal_id}")
async def get_by_id(animal_id: int, session=Depends(get_session)):
    service = AnimalService(session)
    return await service.get_by_id(animal_id)


@router.get("/{brinco}")
async def get_by_brinco(brinco: str, session=Depends(get_session)):
    service = AnimalService(session)
    return await service.get_by_field("brinco", brinco)


@router.get("/{chip}")
async def get_by_chip(chip: str, session=Depends(get_session)):
    service = AnimalService(session)
    return await service.get_by_field("chip", chip)


@router.get("/")
async def get_all(session=Depends(get_session)):
    service = AnimalService(session)
    return await service.get_all()


@router.patch("/{animal_id}")
async def update(animal_id: int, animal: AnimalUpdate,
                 session=Depends(get_session)):
    service = AnimalService(session)
    return await service.update(animal_id, animal)


@router.delete("/{animal_id}")
async def delete(animal_id: int, service=Depends(AnimalService)) -> dict:
    return await service.delete(animal_id)
