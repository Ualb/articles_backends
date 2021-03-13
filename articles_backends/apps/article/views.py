from rest_framework import viewsets
from .models import Article
from .serializer import ArticleSerializer


class ArticleView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
