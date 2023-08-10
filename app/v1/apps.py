from pathlib import Path

from django.apps import AppConfig


class APIConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = Path(__file__).resolve().parent.parent
    BASIC_CACHE_TIMEOUT = 60
    REQUEST_TIMEOUT = 60
