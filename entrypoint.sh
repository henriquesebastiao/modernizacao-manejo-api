#!/bin/sh

alembic upgrade head

if [ "$DEBUG" -eq 1 ]; then
  fastapi run --reload app/main.py
else
  fastapi run --workers 4 app/main.py
fi