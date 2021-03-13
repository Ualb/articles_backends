from .serializer import PaymentSerializer
from rest_framework.response import Response
from rest_framework import status


def payment_validator(data):
    raw_shop = PaymentSerializer(data=data)
    if payment.is_valid():
        return Response(
            {
                "Message": "fields incomplete"
            }, status=status.HTTP_400_BAD_REQUEST
        )
    return True
