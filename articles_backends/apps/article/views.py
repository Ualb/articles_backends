from rest_framework import viewsets, status, filters
from rest_framework.response import Response

from .models import Article
from .serializer import ArticleSerializer
from .constraints import article_validator
from apps.article.logic.article import update_article, delete_article


class ArticleView(viewsets.ModelViewSet):
    queryset = Article.objects.filter(is_active=True)
    serializer_class = ArticleSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['code']
    http_method_names = ['get', 'post', 'put', 'delete']

    def update(self, request):
        is_valid, article = article_validator(request.data)
        if is_valid:
            update_article(request.data, article)
            return Response(ArticleSerializer(article).data, status=status.HTTP_200_OK)
        else:
            return Response({'Message': 'The Article Is Not Fount.'},
                            status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request):
        is_valid, article = article_validator(request.data)
        if is_valid:
            delete_article(article)
            return Response({'Message': 'The Article Does Not Exist'}, status=status.HTTP_200_OK)
        else:
            return Response({'Message': 'The Article Is Not Fount.'},
                            status=status.HTTP_404_NOT_FOUND)
