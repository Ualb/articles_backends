from rest_framework.response import Response
from rest_framework import status

from .serializer import PaymentSerializer
from apps.article.models import Article


def payment_validator(data):
    raw_shop = PaymentSerializer(data=data)
    if raw_shop.is_valid():
        return Response(
            {
                "Message": "fields incomplete"
            }, status=status.HTTP_400_BAD_REQUEST
        )
    return True


def articles_validator(id):
    try:
        Article.objects.get(id=id)
        return True
    except Exception as ex:
        return False
