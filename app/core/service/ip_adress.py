import logging

from rest_framework.request import Request


def get_ip(request: Request):
    """Основна функія на отримання IP клієнта, з якого був надісланий запит"""
    origin_header = 'X-Original-Forwarded-For'
    remote_header = 'REMOTE_ADDR'

    if ip_address := request.headers.get(origin_header):
        return ip_address

    elif ip_address := request.META.get(remote_header):
        logging.warning(
            'Failed to get valid IP address from header "%s". '
            'The IP of the server obtained from the "%s" header will be used instead. '
            'Request: %s' % (origin_header, remote_header, request.stream.__repr__())
        )
        return ip_address

    raise ValueError('Failed to get remote IP address')
