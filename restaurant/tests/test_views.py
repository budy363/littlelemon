from django.test import TestCase
from rest_framework.test import APIClient

class MenuViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_menu_endpoint(self):
        response = self.client.get('/api/menu/')
        self.assertEqual(response.status_code, 200)
