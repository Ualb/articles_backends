from rest_framework import viewsets, status, filters
from rest_framework.response import Response

from .models import Article
from .serializer import ArticleSerializer


class ArticleView(viewsets.ModelViewSet):
    queryset = Article.objects.filter(is_active=True)
    serializer_class = ArticleSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['code']
    http_method_names = ['get', 'post', 'put', 'delete']

    def update(self, request):
        raw_article = ArticleSerializer(data=request.data)
        if article.is_valid():
            try:
                article = Article.objects.get(code=raw_article.data['code'])
            except Exception as ex:
                return Response({'Message': 'The Article Is Not Fount.'},
                                status=status.HTTP_404_NOT_FOUND)
            article.description = raw_article.data['description']
            article.price = raw_article.data['price']
            article.cost = raw_article.data['cost']
            article.is_active = raw_article.data['is_active']
            article.save()
            return Response(ArticleSerializer(article).data, status=status.HTTP_200_OK)

    def destroy(self, request):
        raw_article = ArticleSerializer(data=request.data)
        if article.is_valid():
            try:
                article = Article.objects.get(code=raw_article.data['code'])
            except Exception as ex:
                return Response({'Message': 'The Article Is Not Fount.'},
                                status=status.HTTP_404_NOT_FOUND)
            article.delete()
            return Response({'Message': 'The Article Does Not Exist'}, status=status.HTTP_200_OK)
