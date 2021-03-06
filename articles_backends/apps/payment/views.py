from rest_framework import viewsets, status, filters
from rest_framework.response import Response

from .models import Payment
from .serializer import PaymentSerializer
from .constraints import payment_validator
from apps.payment.logic.payment import save_payment
from apps.common.paginator import DefaultPagination


class PaymentView(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['date']
    http_method_names = ['get', 'post']
    pagination_class = DefaultPagination

    def create(self, request):
        if payment_validator(request.data):
            payment = save_payment(request.data)
            return Response(
                PaymentSerializer(
                    payment).data, status=status.HTTP_201_CREATED
            )
