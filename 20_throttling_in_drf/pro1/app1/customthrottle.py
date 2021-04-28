from rest_framework.throttling import UserRateThrottle


class dummythrottle(UserRateThrottle):
    scope = 'dummy'
