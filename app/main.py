from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import animal, login, user, user_type

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
app.include_router(login.router)
app.include_router(user_type.router)
app.include_router(user.router)
