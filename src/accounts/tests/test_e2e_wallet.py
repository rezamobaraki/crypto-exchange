from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from accounts.models import Wallet
from django.contrib.auth.models import User
from decimal import Decimal

class WalletE2ETestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.wallet = Wallet.objects.create(user=self.user, balance=Decimal('100.00'))
        self.client.login(username='testuser', password='12345')

    def test_deposit_success(self):
        # Simulate depositing into the wallet
        url = reverse('api-v1:accounts:wallet:wallet-deposit', args=[self.wallet.id])
        data = {'amount': '50.00'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.wallet.refresh_from_db()
        self.assertEqual(self.wallet.balance, Decimal('150.00'))

    def test_deposit_negative_value(self):
        url = reverse('api-v1:accounts:wallet:wallet-deposit', args=[self.wallet.id])
        data = {'amount': '-50.00'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
