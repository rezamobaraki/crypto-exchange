from decimal import Decimal

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from exchanges.models.crypto_currency import CryptoCurrency


class CryptoCurrencyE2ETestCase(APITestCase):

    def setUp(self):
        # Create a few cryptocurrencies
        CryptoCurrency.objects.create(name='ABAN', price=Decimal('5.00'))
        CryptoCurrency.objects.create(name='BTC', price=Decimal('50000.00'))

    def test_list_cryptocurrencies(self):
        # Test the listing endpoint for crypto currencies
        url = reverse('api-v1:exchanges:crypto_currency:cryptocurrency-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # We created 2 cryptocurrencies
