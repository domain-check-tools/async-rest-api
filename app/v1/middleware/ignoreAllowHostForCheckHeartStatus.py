from django.http import HttpRequest


class IgnoreAllowedHostsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        if '/healthz/' in request.path:
            request.META['HTTP_HOST'] = 'healthz'
        return self.get_response(request)
