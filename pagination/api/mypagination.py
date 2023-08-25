from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 5 #Num of items to be shown. Here 5 items per page
    page_query_param = 'p'
    page_size_query_param = 'records'
    max_page_size = 7
