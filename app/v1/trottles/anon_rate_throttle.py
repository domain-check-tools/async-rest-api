from rest_framework.throttling import AnonRateThrottle


class PostAnonRateThrottle(AnonRateThrottle):
    rate = '120/min'


class GetAnonRateThrottle(AnonRateThrottle):
    rate = '150/min'
