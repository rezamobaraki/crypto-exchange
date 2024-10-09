from decimal import Decimal
from django.contrib.auth.models import User
from django.test import override_settings
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from accounts.models import Wallet
from transactions.models.transaction import Transaction
from django.contrib.contenttypes.models import ContentType


@override_settings(DJANGO_SETTINGS_MODULE='core.settings.django.test')
class TransactionE2ETestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.wallet = Wallet.objects.create(user=self.user, balance=Decimal('100.00'))
        content_type = ContentType.objects.get_for_model(Wallet)
        self.transaction1 = Transaction.objects.create(wallet=self.wallet, amount=Decimal('10.00'), type='DEPOSIT', content_type=content_type, object_id=self.wallet.id)
        self.transaction2 = Transaction.objects.create(wallet=self.wallet, amount=Decimal('50.00'), type='WITHDRAWAL', content_type=content_type, object_id=self.wallet.id)
        self.client.login(username='testuser', password='12345')

    def test_list_transactions(self):
        url = reverse('api-v1:transactions:transaction-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_view_single_transaction(self):
        url = reverse('api-v1:transactions:transaction-detail', args=[self.transaction1.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['amount'], '10.00')
        self.assertEqual(response.data['type'], 'DEPOSIT')
