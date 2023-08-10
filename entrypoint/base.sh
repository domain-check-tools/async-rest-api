#!/usr/bin/env bash

DJANGO_DIR=/app

DJANGO_ASGI_MODULE=app.asgi

echo "Starting $NAME as $(whoami)"

# Activate the virtual environment
cd $DJANGO_DIR

export PYTHONPATH=$DJANGO_DIR:$PYTHONPATH