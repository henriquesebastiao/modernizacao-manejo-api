from fastapi import APIRouter, Depends

from app.schemas.animal import AnimalCreate, AnimalSchema, AnimalUpdate
from app.services.animal import AnimalService

router = APIRouter(prefix="/animal", tags=["Animal"])


@router.post("/", response_model=AnimalSchema, status_code=201)
async def create(cargo: AnimalCreate, service=Depends(AnimalService)):
    return service.create(cargo)


@router.get("/{animal_id}", response_model=AnimalSchema)
def get_by_id(animal_id: int, service=Depends(AnimalService)):
    return service.get_by_id(animal_id)


@router.get("/{brinco}", response_model=AnimalSchema)
def get_by_brinco(brinco: str, service=Depends(AnimalService)):
    return service.get_by_field("brinco", brinco)


@router.get("/{chip}", response_model=AnimalSchema)
def get_by_chip(chip: str, service=Depends(AnimalService)):
    return service.get_by_field("chip", chip)


@router.get("/", response_model=list[AnimalSchema])
async def get_all(service=Depends(AnimalService)):
    return service.get_all()


@router.patch("/{animal_id}")
async def update(animal_id: int, animal: AnimalUpdate,
                 service=Depends(AnimalService)):
    return service.update(animal_id, animal)


@router.delete("/{animal_id}")
async def delete(animal_id: int, service=Depends(AnimalService)) -> dict:
    return service.delete(animal_id)
