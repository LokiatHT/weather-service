from django.test import TestCase, Client
from .models import UserAPIKey
import json

class WeatherAPITests(TestCase):
    def setUp(self):
        self.client = Client()
        self.api_key = UserAPIKey.objects.create().api_key

    def test_register_user(self):
        response = self.client.post('/register')
        self.assertEqual(response.status_code, 200)
        self.assertIn('api_key', response.json())

    def test_multi_city_weather_with_api_key(self):
        cities = {"cities": ["London", "Mumbai"]}
        response = self.client.post(
            '/multi',
            data=json.dumps(cities),
            content_type='application/json',
            **{"HTTP_X_API_KEY": self.api_key}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn('results', response.json())
