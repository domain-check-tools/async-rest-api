import logging

from adrf.views import APIView
from asgiref.sync import async_to_sync
from django.urls import path
from rest_framework.request import Request
from rest_framework.response import Response

logger = logging.getLogger(__name__)


class StatusCheck(APIView):
    @async_to_sync
    async def get(self, request: Request):
        return Response(dict(
            msg='ok'
        ))


urlpatterns = [
    path('', StatusCheck.as_view()),
]