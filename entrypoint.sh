#!/bin/sh

export TEST=0

alembic upgrade head
uvicorn --host 0.0.0.0 app.main:app