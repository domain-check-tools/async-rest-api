from rest_framework import status
from rest_framework.exceptions import ValidationError


class EntryValue(ValidationError):
    status_code = status.HTTP_418_IM_A_TEAPOT