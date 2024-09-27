from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from exchanges.models.crypto_currency import CryptoCurrency
from accounts.models import Wallet
from decimal import Decimal

class OrderE2ETestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.crypto = CryptoCurrency.objects.create(name='ABAN', price=Decimal('5.00'))
        self.wallet = Wallet.objects.create(user=self.user, balance=Decimal('100.00'))
        self.client.login(username='testuser', password='12345')

    def test_create_order_success(self):
        url = reverse('api-v1:orders:order-list')
        data = {'crypto': self.crypto.id, 'amount': '10.00'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.wallet.refresh_from_db()
        self.assertEqual(self.wallet.balance, Decimal('50.00'))  # 50 left after buying 10 ABAN (5*10=50)

    def test_create_order_insufficient_balance(self):
        url = reverse('api-v1:orders:order-list')
        data = {'crypto': self.crypto.id, 'amount': '50.00'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
