"""Modulo principal da aplicação."""

from fastapi import FastAPI

from app.database import Base, engine
from app.routes import animal, cargo, fazenda, fazendeiro, lote, pesagem, \
    usuario
from app.routes import pessoa

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    """Cria as tabelas do banco de dados."""
    Base.metadata.create_all(engine)


app.include_router(animal.router, tags=["animal"])
app.include_router(cargo.router, tags=["cargo"])
app.include_router(e.router, tags=["fazenda"])
app.include_router(fazendeiro.router, tags=["fazendeiro"])
app.include_router(lote.router, tags=["lote"])
app.include_router(pesagem.router, tags=["pesagem"])
app.include_router(pessoa.router, tags=["pessoa"])
app.include_router(usuario.router, tags=["usuario"])
