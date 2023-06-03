from fastapi import FastAPI

from database.db import engine
from models.animal import Base
from routes import animal, cargo, db, fazenda, usuario, pessoa
from models.fazendeiro import Fazendeiro
from models.fazenda import Fazenda
from models.usuario import Usuario
from models.pessoa import Pessoa

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(engine)


app.include_router(animal.router, tags=["animal"])
app.include_router(cargo.router, tags=["cargo"])
app.include_router(fazenda.router, tags=["fazenda"])
app.include_router(usuario.router, tags=["usuario"])
app.include_router(pessoa.router, tags=["pessoa"])
app.include_router(db.router, tags=["db"])
