#!/usr/bin/env bash
NAME="api"

source entrypoint/base.sh

# Start your Django Unicorn
exec uvicorn ${DJANGO_ASGI_MODULE}:application \
  --host 0.0.0.0 \
  --port 8000 \
  --log-level=debug