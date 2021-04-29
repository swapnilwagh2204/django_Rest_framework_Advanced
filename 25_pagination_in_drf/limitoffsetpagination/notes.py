# pagination:
# drf supports support for customizable pagination styles.
# this allows you to modify how large result set are split into individual pages of data.
import rest_framework

# pagination types:
# 1.PageNumberPagination
# 2.limit offset pagination
# 3.cursorpagination


# global settingss:
# pagination style may be set globlally, using the DEFAULT_PAGINATION_CLASS AND PAGE_SIZE setting keys.

# REST_FRAMEWORK = {
# 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
# 'PAGE_SIZE': 5
# }


# pagination per view:
# You can set the pagination class on an individual view by using the pagination_class attribute.
# class StudentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     pagination_class = PageNumberPagination


# PageNumberPagination:
# This pagination style accepts a single number page number in the request query parameters.
# To enable the PageNumberPagination style globally, use the following configuration, and set the PAGE_SIZE as desired:
# REST_FRAMEWORK = {
#     'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
#     'PAGE_SIZE’: 5
# }

# http://127.0.0.1:8000/studentapi/?page=3


# The PageNumberPagination class includes a number of attributes that may be overridden to modify the pagination style.
# To set these attributes you should override the PageNumberPagination class, and then enable your custom pagination class.
# django_paginator_class - The Django Paginator class to use. Default is django.core.paginator.Paginator, which should be fine for most use cases.
# page_size - A numeric value indicating the page size. If set, this overrides the PAGE_SIZE setting. Defaults to the same value as the PAGE_SIZE settings key.
# page_query_param - A string value indicating the name of the query parameter to use for the pagination control.
# page_size_query_param - If set, this is a string value indicating the name of a query parameter that allows the client to set the page size on a per-request basis. Defaults to None, indicating that the client may not control the requested page size.


# max_page_size - If set, this is a numeric value indicating the maximum allowable requested page size. This attribute is only valid if page_size_query_param is also set.
# last_page_strings - A list or tuple of string values indicating values that may be used with the page_query_param to request the final page in the set. Defaults to ('last',)
# template - The name of a template to use when rendering pagination controls in the browsable API. May be overridden to modify the rendering style, or set to None to disable HTML pagination controls completely. Defaults to "rest_framework/pagination/numbers.html".

# class MyPageNumberPagination(PageNumberPagination):
#     page_size = 5
#     page_size_query_param = ‘records'
#     max_page_size = 7

# class StudentList(ListAPIView):
#    queryset = Student.objects.all()
#    serializer_class = StudentSerializer
#    pagination_class = MyPageNumberPagination


# LimitOffsetPagination:
# This pagination style mirrors the syntax used when looking up multiple database records. The client includes both a "limit" and an "offset" query parameter. The limit indicates the maximum number of items to return, and is equivalent to the page_size in other styles. The offset indicates the starting position of the query in relation to the complete set of unpaginated items.
# To enable the LimitOffsetPagination style globally, use the following configuration:
# REST_FRAMEWORK = {
#     'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination’
# }

# http://127.0.0.1:8000/studentapi/?limit=4&offset=6


# The LimitOffsetPagination class includes a number of attributes that may be overridden to modify the pagination style.
# To set these attributes you should override the LimitOffsetPagination class, and then enable your custom pagination class.
# default_limit - A numeric value indicating the limit to use if one is not provided by the client in a query parameter. Defaults to the same value as the PAGE_SIZE settings key.
# limit_query_param - A string value indicating the name of the "limit" query parameter. Defaults to 'limit'.
# offset_query_param - A string value indicating the name of the "offset" query parameter. Defaults to 'offset'.


# max_limit - If set this is a numeric value indicating the maximum allowable limit that may be requested by the client. Defaults to None.
# template - The name of a template to use when rendering pagination controls in the browsable API. May be overridden to modify the rendering style, or set to None to disable HTML pagination controls completely. Defaults to "rest_framework/pagination/numbers.html".


# CursorPagination:


# The cursor-based pagination presents an opaque "cursor" indicator that the client may use to page through the result set. This pagination style only presents forward and reverse controls, and does not allow the client to navigate to arbitrary positions.
# Cursor based pagination requires that there is a unique, unchanging ordering of items in the result set. This ordering might typically be a creation timestamp on the records, as this presents a consistent ordering to paginate against.
# The default is to order by "-created". This assumes that there must be a 'created' timestamp field on the model instances, and will present a "timeline" style paginated view, with the most recently added items first.

# The CursorPagination class includes a number of attributes that may be overridden to modify the pagination style.
# To set these attributes you should override the CursorPagination class, and then enable your custom pagination class.
# page_size = A numeric value indicating the page size. If set, this overrides the PAGE_SIZE setting. Defaults to the same value as the PAGE_SIZE settings key.
# cursor_query_param = A string value indicating the name of the "cursor" query parameter. Defaults to 'cursor'.
# ordering = This should be a string, or list of strings, indicating the field against which the cursor based pagination will be applied. For example: ordering = 'slug'. Defaults to -created. This value may also be overridden by using OrderingFilter on the view.
