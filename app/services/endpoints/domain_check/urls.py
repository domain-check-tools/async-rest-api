from django.urls import path

from core.service.cache import cached_view
from .views import Test
from ...apps import APIConfig

urlpatterns = [
    path('', Test.as_view()),
    path('test_cache/', cached_view(timeout=APIConfig.BASIC_CACHE_TIMEOUT)(
        Test.as_view()
    ))
]
