from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute

from app.core.settings import get_settings
from app.routes import (
    animal,
    animal_weight,
    batch,
    batch_log,
    employment,
    farm,
    farmer,
    token,
    user,
)
from app.settings import get_settings


def custom_generate_unique_id(route: APIRoute):
    return f'{route.tags[0]}-{route.name}'


settings = get_settings()

description = f"""
Modernização Manejo
#### Documentação alternativa: [Redoc]({settings.APP_URL}/redoc)
"""

app = FastAPI(
    docs_url='/',
    generate_unique_id_function=custom_generate_unique_id,
    title='Manejo API',
    description=description,
    version=settings.VERSION,
    terms_of_service='https://github.com/henriquesebastiao/modernizacao-manejo-api/',
    contact={
        'name': 'Manejo API',
        'url': 'https://github.com/henriquesebastiao/modernizacao-manejo-api',
        'email': 'contato@henriquesebastiao.com',
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
app.include_router(farmer.router)
app.include_router(farm.router)
app.include_router(employment.router)
app.include_router(batch.router)
app.include_router(batch_log.router)
app.include_router(animal.router)
app.include_router(animal_weight.router)
app.include_router(token.router)
