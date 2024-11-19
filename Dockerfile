FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY . /code/

RUN pip install --no-cache-dir --root-user-action ignore --upgrade pip \
    && pip install --no-cache-dir --root-user-action ignore -r requirements.txt

RUN opentelemetry-bootstrap -a install

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]