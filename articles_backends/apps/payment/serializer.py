from rest_framework import serializers

from .models import Payment, PaymentDetail
from apps.article.serializer import ArticleSerializer


class PaymentDetailSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=False, read_only=True)

    class Meta:
        model = PaymentDetail
        fields = (
            'id',
            'id_article',
            'id_payment',
            'quantity',
            'sub_total',
            'articles'
        )


class PaymentSerializer(serializers.ModelSerializer):
    payment_detail = PaymentDetailSerializer(
        many=True, allow_null=True)

    class Meta:
        model = Payment
        fields = (
            'id',
            'date',
            'payment_detail'
        )
