from rest_framework import serializers
from .models import Payment, PaymentDetail


class PaymentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetail
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    payment_detail = PaymentDetailSerializer(many=True)

    class Meta:
        model = Payment
        fields = (
            'id',
            'date',
            'payment_detail'
        )
