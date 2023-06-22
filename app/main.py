from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute

from app.routes import animal, animal_weight, animal_weight_type, batch, \
    batch_log, breed, employment, employment_position, farm, farmer, \
    farmer_plan, login, user, user_type


def custom_generate_unique_id(route: APIRoute):
    return f"{route.tags[0]}-{route.name}"


app = FastAPI(generate_unique_id_function=custom_generate_unique_id,
              title="Manejo API", description="Modernização manejo",
              version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Root"])
async def root():
    """Rota principal."""
    return {"message": "Hello World"}


app.include_router(animal.router)
app.include_router(animal_weight.router)
app.include_router(animal_weight_type.router)
app.include_router(batch.router)
app.include_router(batch_log.router)
app.include_router(breed.router)
app.include_router(employment.router)
app.include_router(employment_position.router)
app.include_router(farm.router)
app.include_router(farmer.router)
app.include_router(farmer_plan.router)
app.include_router(login.router)
app.include_router(user_type.router)
app.include_router(user.router)
