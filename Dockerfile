FROM python:3.13-slim

ENV POETRY_VIRTUALENVS_CREATE=false
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY . .

RUN pip install poetry
RUN poetry config installer.max-workers 10
RUN poetry install --without dev --no-interaction --no-ansi

EXPOSE 8000

CMD poetry run uvicorn --host 0.0.0.0 app.main:app