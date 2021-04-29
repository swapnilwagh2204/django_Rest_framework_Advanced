from rest_framework.pagination import CursorPagination, LimitOffsetPagination, PageNumberPagination


class Mypaginationsettings(PageNumberPagination):
    page_size = 3,
    page_query_param = 'p',
    page_size_query_param = 'records',
    max_page_size = 4
    last_page_strings = 'end'


class Myoffsetpaginationsettings(LimitOffsetPagination):
    default_limit = 2
    limit_query_param = 'mylimit'
    offset_query_param = 'myoffset'
    max_limit = 3


class MyCursorPaginationsettings(CursorPagination):
    page_size = 3
    ordering = 'name'
    cursor_query_param = 'cu'
