from adrf.views import APIView
from asgiref.sync import async_to_sync
from rest_framework.request import Request
from rest_framework.response import Response


class Test(APIView):
    """Test"""

    @async_to_sync
    async def get(self, request: Request):
        return Response({'test': 1})
