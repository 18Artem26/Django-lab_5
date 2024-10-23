from django.test import TestCase
from django.urls import reverse

class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')  # Переконайтесь, що URL 'home' існує у вашому urls.py
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
