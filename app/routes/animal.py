from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import Repository
from app.database import get_session
from app.models.animal import Animal
from app.schemas.animal import AnimalSchema

router = APIRouter(prefix="/animal", tags=["Animal"])


class Message(BaseModel):
    detail: str


@router.post("/", response_model=AnimalSchema,
             responses={404: {"model": Message,
                              "description": "Animal already exists"},
                        500: {"model": Message,
                              "description": "Internal Server Error"}})
async def create(schema: AnimalSchema, db: AsyncSession = Depends(get_session)):
    try:
        repository = Repository(Animal, AnimalSchema, db)
        db_animal = await repository.create(schema)
    except IntegrityError:
        raise HTTPException(status_code=404, detail="Animal already exists")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    await repository.commit()
    return db_animal


@router.get("/{animal_id}")
async def get_by(animal_id: int, db: AsyncSession = Depends(get_session)):
    repository = Repository(Animal, AnimalSchema, db)
    db_animal = await repository.get(animal_id)
    return db_animal


@router.get("/")
async def get_all(db: AsyncSession = Depends(get_session)):
    repository = Repository(Animal, AnimalSchema, db)
    db_animal = await repository.get_all()
    return db_animal


@router.patch("/{animal_id}")
async def update(animal_id: int, animal: AnimalSchema,
                 db: AsyncSession = Depends(get_session)):
    repository = Repository(Animal, AnimalSchema, db)
    db_animal = await repository.update(animal_id, animal)
    await repository.commit()
    return db_animal


@router.delete("/{animal_id}")
async def delete(animal_id: int, db: AsyncSession = Depends(get_session)):
    repository = Repository(Animal, AnimalSchema, db)
    db_animal = await repository.delete(animal_id)
    await repository.commit()
    return db_animal
