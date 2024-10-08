from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute

from app.routes import (
    animal,
    animal_weight,
    animal_weight_type,
    batch,
    batch_log,
    breed,
    employment,
    employment_position,
    farm,
    farmer,
    token,
    user,
)


def custom_generate_unique_id(route: APIRoute):
    return f'{route.tags[0]}-{route.name}'


description = """
Modernização Manejo
#### Documentação alternativa: [Redoc](https://api.henriquesebastiao.com/redoc)
"""

app = FastAPI(
    docs_url='/',
    generate_unique_id_function=custom_generate_unique_id,
    title='Manejo API',
    description=description,
    version='0.1.0',
    terms_of_service='https://site.henriquesebastiao.com/',
    contact={
        'name': 'Manejo API',
        'url': 'https://api.henriquesebastiao.com/',
        'email': 'ivan@noleto.tech',
    },
    license_info={
        'name': 'Apache 2.0',
        'url': 'https://www.apache.org/licenses/LICENSE-2.0.html',
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(user.router)
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
app.include_router(token.router)
