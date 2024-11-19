import logging

import uvicorn
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
from app.telemetry import PrometheusMiddleware, metrics, setting_otlp


def custom_generate_unique_id(route: APIRoute):
    return f'{route.tags[0]}-{route.name}'


settings = get_settings()

APP_NAME = settings.APP_NAME
OTLP_GRPC_ENDPOINT = settings.OTLP_GRPC_ENDPOINT

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

# Setting metrics middleware
app.add_middleware(PrometheusMiddleware, app_name=APP_NAME)
app.add_route('/metrics', metrics)

if not settings.TEST:
    # Setting OpenTelemetry exporter
    setting_otlp(app, APP_NAME, OTLP_GRPC_ENDPOINT)


class EndpointFilter(logging.Filter):
    # Uvicorn endpoint access log filter
    def filter(self, record: logging.LogRecord) -> bool:
        return record.getMessage().find('GET /metrics') == -1


# Filter out /endpoint
logging.getLogger('uvicorn.access').addFilter(EndpointFilter())

app.include_router(user.router)
app.include_router(farmer.router)
app.include_router(farm.router)
app.include_router(employment.router)
app.include_router(batch.router)
app.include_router(batch_log.router)
app.include_router(animal.router)
app.include_router(animal_weight.router)
app.include_router(token.router)


if __name__ == '__main__':
    # update uvicorn access logger format
    log_config = uvicorn.config.LOGGING_CONFIG
    log_config['formatters']['access']['fmt'] = (
        '%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] [trace_id=%(otelTraceID)s span_id=%(otelSpanID)s resource.service.name=%(otelServiceName)s] - %(message)s'
    )
    if settings.DEBUG:
        uvicorn.run(
            'main:app',
            host=settings.APP_BIND_HOST,
            port=settings.EXPOSE_PORT,
            reload=True,
            log_config=log_config,
        )
    else:
        uvicorn.run(
            'main:app',
            host=settings.APP_BIND_HOST,
            port=settings.EXPOSE_PORT,
            workers=4,
            log_config=log_config,
        )
