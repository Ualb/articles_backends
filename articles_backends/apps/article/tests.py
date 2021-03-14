from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from apps.article.models import Article


class TestView(APITestCase):

    api_client = APIClient()

    def create_article(self):
        return Article(
            code='0001A',
            description='I Have Hungry',
            price=90.12,
            cost=2.87
        ).save()

    def test_post_article(self):
        article = {
            'code': '0001',
            'description': 'I Love Programmer in Python',
            'price': 100.12,
            'cost': 23.2
        }
        response = self.api_client.post(
            '/api/articles/', article, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_article(self):
        self.create_article()
        response = self.api_client.get(
            '/api/articles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_update_article(self):
    #     self.create_article()
    #     article_upgrade = {
    #         'code': '0001A',
    #         'description': 'I Love Programmer in Python',
    #         'price': 50.5,
    #         'cost': 23.2
    #     }
    #     response = self.api_client.put(
    #         '/api/articles/', article_upgrade, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_delete_article(self):
    #     self.create_article()
    #     response = self.api_client.delete(
    #         '/api/articles/', {'code': '0001A'}, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
