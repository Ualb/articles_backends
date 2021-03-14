
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from apps.payment.models import Payment, PaymentDetail
from apps.article.models import Article


class TestView(APITestCase):

    api_client = APIClient()

    def create_article(self, code, price):
        return Article(
            code=code,
            description='I Have Hungry',
            price=price,
            cost=2.87
        ).save()

    def create_payment(self):
        return Payment().save()

    def test_post_payment(self):
        self.create_article('000X2', 90.2)
        payment = {
            'payment_detail': [
                {
                    'id_article': 1,
                    'quantity': 10
                },
            ]
        }
        response = self.api_client.post(
            '/api/payments/', payment, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
