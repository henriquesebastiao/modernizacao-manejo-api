from fastapi import APIRouter

from database.db import session
from models.cargo import Cargo
from serializer.cargo import CargoSerializer

router = APIRouter()


@router.post("/cargo")
async def create_cargo(cargo: CargoSerializer):
    cargo_db = Cargo(
        nome=cargo.nome,
    )

    session.add(cargo_db)
    session.commit()

    return {"message": f"Cargo {cargo.nome} criado com sucesso!"}


@router.delete("/cargo/{id}")
async def delete_cargo(id: int):
    cargo_db = session.query(Cargo).filter(Cargo.id == id).first()
    session.delete(cargo_db)
    session.commit()
    return {"message": f"Cargo {cargo_db.nome} deletado com sucesso!"}
