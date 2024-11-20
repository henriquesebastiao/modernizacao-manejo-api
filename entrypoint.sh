#!/bin/sh

export OTEL_SERVICE_NAME=app-manejo
export OTEL_EXPORTER_OTLP_ENDPOINT=loki-manejo:4317
export OTEL_EXPORTER_OTLP_INSECURE=true
export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
export OTEL_TRACES_EXPORTER=otlp
export OTEL_METRICS_EXPORTER=otlp
export OTEL_LOGS_EXPORTER=otlp
export PYTHON_COLORS=0

export TEST=0

alembic upgrade head
opentelemetry-instrument python app/main.py