from drf_standardized_errors.formatter import ExceptionFormatter
from drf_standardized_errors.types import ErrorResponse

from v1.services.create_responce import Status


class MyExceptionFormatter(ExceptionFormatter):
    """
        {
           "status": "error",
           "type": "validation_error",
           "errors": [
             {
              "code": "required",
              "detail": "This field is required.",
              "attr": "name"
             },
           ]
        }

    """

    def format_error_response(self, error_response: ErrorResponse):
        error = super().format_error_response(error_response)

        data = {
            "status": Status.ERROR.value,
            "type": error['type'],
            "errors": error['errors']
        }
        return data
