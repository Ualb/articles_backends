from rest_framework import viewsets, status, filters
from rest_framework.response import Response

from .models import Article
from .serializer import ArticleSerializer
from apps.common.paginator import DefaultPagination


class ArticleView(viewsets.ModelViewSet):
    queryset = Article.objects.filter(is_active=True)
    serializer_class = ArticleSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['code']
    pagination_class = DefaultPagination
