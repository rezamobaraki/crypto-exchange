from django.contrib.auth.models import User
from django.test import override_settings
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


@override_settings(DJANGO_SETTINGS_MODULE='core.settings.django.test')
class AuthE2ETestCase(APITestCase):

    def test_register_success(self):
        url = reverse('api-v1:accounts:authentication:register-list')
        data = {'username': 'newuser', 'password': 'password123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access_token', response.data)
        self.assertIn('refresh_token', response.data)

    def test_login_success(self):
        User.objects.create_user(username='testuser', password='12345')
        url = reverse('api-v1:accounts:authentication:login-list')
        data = {'username': 'testuser', 'password': '12345'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access_token', response.data)
        self.assertIn('refresh_token', response.data)

    def test_login_invalid_credentials(self):
        url = reverse('api-v1:accounts:authentication:login-list')
        data = {'username': 'wronguser', 'password': 'wrongpass'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
