from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import Repository
from app.database import get_session
from app.models.employment import EmploymentPosition
from app.schemas.employment import EmploymentPositionSchema

router = APIRouter(prefix='/employment/position', tags=['Employment Position'])


@router.post('/', status_code=201)
async def create(
    schema: EmploymentPositionSchema, db: AsyncSession = Depends(get_session)
):
    """
    Adiciona um novo cargo

    - **name (str)**: Nome do cargo
    """
    repository = Repository(EmploymentPosition, db)
    db_employment_position = await repository.create(**schema.dict())
    await repository.commit()
    return db_employment_position


@router.get('/{employment_position_id}')
async def get_by(
    employment_position_id: int, db: AsyncSession = Depends(get_session)
):
    """Retorna um cargo pelo seu ID."""
    repository = Repository(EmploymentPosition, db)
    db_employment_position = await repository.get(employment_position_id)
    return db_employment_position


@router.get('/')
async def get_all(db: AsyncSession = Depends(get_session)):
    """Retorna todos os cargos."""
    repository = Repository(EmploymentPosition, db)
    db_employment_position = await repository.get_all()
    return db_employment_position


@router.patch('/{employment_position_id}')
async def update(
    employment_position_id: int,
    schema: EmploymentPositionSchema,
    db: AsyncSession = Depends(get_session),
):
    """
    Atualiza um cargo

    - **name (str)**: Nome do cargo
    """
    repository = Repository(EmploymentPosition, db)
    db_employment_position = await repository.update(
        employment_position_id, **schema.dict()
    )
    await repository.commit()
    return db_employment_position


@router.delete('/{employment_position_id}')
async def delete(
    employment_position_id: int, db: AsyncSession = Depends(get_session)
):
    """Deleta um cargo pelo seu ID."""
    repository = Repository(EmploymentPosition, db)
    db_employment_position = repository.delete(employment_position_id)
    await repository.commit()
    return db_employment_position
