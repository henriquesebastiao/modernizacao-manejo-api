"""Routes for raca"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.raca import RacaCreateSchema, RacaDeleteSchema, \
    RacaSchema, RacaUpdateSchema
from app.services.raca_service import RacaService

router = APIRouter(prefix="/raca", tags=["Raca"])


@router.post("/", response_model=RacaSchema)
async def create_raca(raca: RacaCreateSchema,
                        db: Session = Depends(get_db)):
    """Cria um raca."""
    raca_service = RacaService(db)
    return raca_service.create_raca(raca)


@router.get("/{raca_id}", response_model=RacaSchema)
def get_raca(raca_id: int, db: Session = Depends(get_db)):
    """Retorna um raca com base no seu ID."""
    raca_service = RacaService(db)
    return raca_service.get_raca(raca_id)


@router.get("/")
async def get_all_racas(db: Session = Depends(get_db)):
    """Retorna todos os animais."""
    raca_service = RacaService(db)
    return raca_service.get_all_racas()


@router.patch("/raca/{raca_id}")
async def update_raca(raca_id: int, raca: RacaUpdateSchema,
                        db: Session = Depends(get_db)):
    """Atualiza um raca."""
    raca_service = RacaService(db)
    return raca_service.update_raca(raca_id, raca)


@router.delete("/raca/{raca_id}")
async def delete_raca(raca: RacaDeleteSchema,
                        db: Session = Depends(get_db)):
    """Deleta um raca."""
    raca_service = RacaService(db)
    raca_service.delete_raca(raca)
    return {"message": "Raca deleted"}
