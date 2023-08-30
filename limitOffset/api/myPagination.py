from rest_framework.pagination import LimitOffsetPagination

class CustomPagination(LimitOffsetPagination):
    default_limit = 10
    limit_query_param = 'l'
    offset_query_param = 'o'
    max_limit = 5
    