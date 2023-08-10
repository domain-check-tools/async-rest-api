#!/usr/bin/env bash
NAME="init"

source entrypoint/base.sh

python manage.py migrate