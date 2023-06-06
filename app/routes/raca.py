"""Routes for raca"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud.raca import create, delete, get_all, get_by_id
from app.database import get_db
from app.schemas.raca import RacaCreate, Raca

router = APIRouter()


@router.post("/raca")
async def create_raca(r: RacaCreate, db: Session = Depends(get_db)):
    """Cria uma raça."""
    return create(r, db)


@router.get("/raca", response_model=list[Raca])
async def get_all_raca(db: Session = Depends(get_db)):
    """Retorna todas as raças."""
    return get_all(db)


@router.get("/raca/{raca_id}", response_model=Raca)
async def get_raca_by_id(raca_id: int, db: Session = Depends(get_db)):
    """Retorna uma raça pelo id."""
    return get_by_id(raca_id, db)


@router.delete("/raca/{raca_id}")
async def delete_raca(raca_id: int, db: Session = Depends(get_db)):
    """Deleta uma raça."""
    return delete(raca_id, db)
