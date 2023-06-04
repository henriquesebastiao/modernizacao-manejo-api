from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.db import get_db
from models.pessoa import Pessoa
from schemas.pessoa import PessoaCreate

router = APIRouter()


@router.post("/pessoa")
async def create_pessoa(pessoa: PessoaCreate, db: Session = Depends(get_db)):
    pessoa_db = Pessoa(
        nome=pessoa.nome,
        sobre_nome=pessoa.sobre_nome,
        cargo_id=pessoa.cargo_id
    )

    db.add(pessoa_db)
    db.commit()

    return {"message": f"Pessoa {pessoa.nome} criada com sucesso!"}


@router.delete("/pessoa/{id}")
async def delete_pessoa(id: int, db: Session = Depends(get_db)):
    pessoa_db = db.query(Pessoa).filter(Pessoa.id == id).first()
    db.delete(pessoa_db)
    db.commit()
    return {"message": f"Pessoa {pessoa_db.nome} deletada com sucesso!"}
