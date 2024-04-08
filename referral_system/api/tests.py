from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status

class TestUserRegistration(APITestCase):
    def test_registration(self):
        url = reverse('registration')
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

# Add tests for user_details and referrals views