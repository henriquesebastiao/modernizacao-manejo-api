from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.cargo import Cargo
from app.schemas.cargo import CargoCreate

router = APIRouter()


@router.post("/cargo")
async def create_cargo(cargo: CargoCreate, db: Session = Depends(get_db)):
    cargo_db = Cargo(
        nome=cargo.nome,
    )

    db.add(cargo_db)
    db.commit()

    return {"message": f"Cargo {cargo.nome} criado com sucesso!"}


@router.delete("/cargo/{id}")
async def delete_cargo(id: int, db: Session = Depends(get_db)):
    cargo_db = db.query(Cargo).filter(Cargo.id == id).first()
    db.delete(cargo_db)
    db.commit()
    return {"message": f"Cargo {cargo_db.nome} deletado com sucesso!"}
