from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import Repository
from app.database import get_session
from app.models.batch import BatchLog
from app.schemas.batch_log import BatchLogSchema

router = APIRouter(prefix='/animal/batch_log', tags=['Animal Batch Log'])


@router.post('/', status_code=201)
async def create(
    schema: BatchLogSchema, db: AsyncSession = Depends(get_session)
):
    """
    Adiciona um novo registro ao log de lotes de animais.

    - **batch_id (int)**: ID do lote.
    - **animal_id (int)**: ID do animal.
    - **entry_date (datetime)**: Data de entrada do animal no lote.
    - **departure_date (datetime)**: Data de saída do animal do lote.
    """
    repository = Repository(BatchLog, db)
    db_batch_log = await repository.create(**schema.dict())
    await repository.commit()
    return db_batch_log


@router.get('/{batch_log_id}')
async def get_by(batch_log_id: int, db: AsyncSession = Depends(get_session)):
    """Retorna um registro do log de lotes de animais com base no ID."""
    repository = Repository(BatchLog, db)
    db_batch_log = await repository.get(batch_log_id)
    return db_batch_log


@router.get('/')
async def get_all(db: AsyncSession = Depends(get_session)):
    """Retorna todos os registros do log de lotes de animais."""
    repository = Repository(BatchLog, db)
    db_batch_log = await repository.get_all()
    return db_batch_log


@router.patch('/{batch_log_id}')
async def update(
    batch_log_id: int,
    schema: BatchLogSchema,
    db: AsyncSession = Depends(get_session),
):
    """
    Atualiza um registro do log de lotes de animais com base no ID.

    - **batch_id (int)**: ID do lote.
    - **animal_id (int)**: ID do animal.
    - **entry_date (datetime)**: Data de entrada do animal no lote.
    - **departure_date (datetime)**: Data de saída do animal do lote.
    """
    repository = Repository(BatchLog, db)
    db_batch_log = await repository.update(batch_log_id, **schema.dict())
    await repository.commit()
    return db_batch_log


@router.delete('/{batch_log_id}')
async def delete(batch_log_id: int, db: AsyncSession = Depends(get_session)):
    """Remove um registro do log de lotes de animais com base no ID."""
    repository = Repository(BatchLog, db)
    db_batch_log = repository.delete(batch_log_id)
    await repository.commit()
    return db_batch_log
