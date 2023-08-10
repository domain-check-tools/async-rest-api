import logging

from cacheops import cached_view as func_cached_view, cached_view_as as func_cached_view_as
from django.conf import settings

logger = logging.getLogger(__name__)


def cached_view(*args, **kwargs):
    def inner_func(func):
        if settings.DISABLE_CACHE:
            return func
        return func_cached_view(*args, **kwargs)(func)

    return inner_func


def cached_view_as(*samples, **kwargs):
    def inner_func(func):
        if settings.DISABLE_CACHE:
            return func
        return func_cached_view_as(*samples, **kwargs)(func)

    return inner_func
