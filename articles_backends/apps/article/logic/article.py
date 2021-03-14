from apps.article.serializer import ArticleSerializer


def update_article(data, article):
    raw_article = ArticleSerializer(data=data)
    article.description = raw_article.data['description']
    article.price = raw_article.data['price']
    article.cost = raw_article.data['cost']
    article.is_active = raw_article.data['is_active']
    article.save()


def delete_article(article):
    article.delete()
