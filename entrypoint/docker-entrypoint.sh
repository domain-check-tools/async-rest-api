#!/usr/bin/env bash
NAME="api"

DJANGO_DIR=/app

DJANGO_ASGI_MODULE=app.asgi

echo "Starting $NAME as $(whoami)"

# Activate the virtual environment
cd $DJANGO_DIR

export PYTHONPATH=$DJANGO_DIR:$PYTHONPATH

python manage.py migrate

# Start your Django Unicorn
exec uvicorn ${DJANGO_ASGI_MODULE}:application \
  --host 0.0.0.0 \
  --port 8000 \
  --log-level=debug