"""Routes for cargo"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.cargo import CargoCreateSchema, CargoDeleteSchema, \
    CargoSchema, CargoUpdateSchema
from app.services.cargo_service import CargoService

router = APIRouter(prefix="/cargo", tags=["Cargo"])


@router.post("/", response_model=CargoSchema)
async def create_cargo(cargo: CargoCreateSchema,
                        db: Session = Depends(get_db)):
    """Cria um cargo."""
    cargo_service = CargoService(db)
    return cargo_service.create_cargo(cargo)


@router.get("/{cargo_id}", response_model=CargoSchema)
def get_cargo(cargo_id: int, db: Session = Depends(get_db)):
    """Retorna um cargo com base no seu ID."""
    cargo_service = CargoService(db)
    return cargo_service.get_cargo(cargo_id)


@router.get("/")
async def get_all_cargos(db: Session = Depends(get_db)):
    """Retorna todos os animais."""
    cargo_service = CargoService(db)
    return cargo_service.get_all_cargos()


@router.patch("/cargo/{cargo_id}")
async def update_cargo(cargo_id: int, cargo: CargoUpdateSchema,
                        db: Session = Depends(get_db)):
    """Atualiza um cargo."""
    cargo_service = CargoService(db)
    return cargo_service.update_cargo(cargo_id, cargo)


@router.delete("/cargo/{cargo_id}")
async def delete_cargo(cargo: CargoDeleteSchema,
                        db: Session = Depends(get_db)):
    """Deleta um cargo."""
    cargo_service = CargoService(db)
    cargo_service.delete_cargo(cargo)
    return {"message": "Cargo deleted"}
