from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import animal, cargo, dieta, fazenda, fazendeiro, login, lote, \
    lote_log, peso_log, pessoa, propriedade, raca, user

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Rota principal."""
    return {"message": "Hello World"}


app.include_router(animal.router)
app.include_router(cargo.router)
app.include_router(dieta.router)
app.include_router(fazenda.router)
app.include_router(fazendeiro.router)
app.include_router(login.router)
app.include_router(lote.router)
app.include_router(lote_log.router)
app.include_router(peso_log.router)
app.include_router(pessoa.router)
app.include_router(propriedade.router)
app.include_router(raca.router)
app.include_router(user.router)
