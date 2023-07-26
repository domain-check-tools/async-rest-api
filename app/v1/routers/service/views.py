from adrf.views import APIView
from asgiref.sync import async_to_sync
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.request import Request
from rest_framework.response import Response

from v1.apps import V1Config


class Test(APIView):
    """Information"""

    @method_decorator(cache_page(V1Config.BASIC_CACHE_TIMEOUT))
    @async_to_sync
    async def get(self, request: Request):
        return Response({'test': 1})
