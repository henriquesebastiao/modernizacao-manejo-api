#!/bin/sh

# O shell irá encerrar a execução do script quando um comando falhar
set -e

while ! nc -z postgres 5432; do
  echo "🟡 Waiting for Postgres Database Startup (postgres:5432) ..."
  sleep 2
done

echo "✅ Postgres Database Started Successfully (postgres:5432)"

uvicorn main:app --reload