from .serializer import ArticleSerializer
from .models import Article


def article_validator(data):
    raw_article = ArticleSerializer(data=data)
    if raw_article.is_valid():
        try:
            article = Article.objects.get(code=raw_article.data['code'])
        except Exception as ex:
            return False
        return True, article
