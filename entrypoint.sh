#!/bin/sh

alembic upgrade head
uvicorn --host 0.0.0.0 app.main:app