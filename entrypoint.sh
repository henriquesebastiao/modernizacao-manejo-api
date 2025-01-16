#!/bin/sh

export TEST=0

alembic upgrade head
python app/main.py