from fastapi import APIRouter

from database.db import session
from models.pessoa import Pessoa
from schemas.pessoa import PessoaCreate

router = APIRouter()


@router.post("/pessoa")
async def create_pessoa(pessoa: PessoaCreate):
    pessoa_db = Pessoa(
        nome=pessoa.nome,
        sobre_nome=pessoa.sobre_nome,
        cargo_id=pessoa.cargo_id
    )

    session.add(pessoa_db)
    session.commit()

    return {"message": f"Pessoa {pessoa.nome} criada com sucesso!"}


@router.delete("/pessoa/{id}")
async def delete_pessoa(id: int):
    pessoa_db = session.query(Pessoa).filter(Pessoa.id == id).first()
    session.delete(pessoa_db)
    session.commit()
    return {"message": f"Pessoa {pessoa_db.nome} deletada com sucesso!"}
