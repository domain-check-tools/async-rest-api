from django.urls import path

from .views import Test
from ...apps import APIConfig
from ...services.cache import cached_view

urlpatterns = [
    path('', Test.as_view()),
    path('test_cache/', cached_view(
        timeout=APIConfig.BASIC_CACHE_TIMEOUT)(
        Test.as_view()
    ),
         )
]
