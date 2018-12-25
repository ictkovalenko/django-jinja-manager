from django.conf import settings
from rest_framework.pagination import PageNumberPagination


class SRSPagination(PageNumberPagination):
    """This class defines all the custom settings that will be used
    to implement SRS pagination"""
    page_size = settings.GLOBAL_PAGE_SIZE
    page_size_query_param = 'size'