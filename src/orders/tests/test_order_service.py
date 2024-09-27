from decimal import Decimal

from django.test import TestCase

from accounts.models import Wallet
from exchanges.models.crypto_currency import CryptoCurrency
from orders.services.order import OrderService


class OrderServiceTestCase(TestCase):

    def setUp(self):
        self.wallet = Wallet.objects.create(balance=Decimal('100.00'))
        self.crypto = CryptoCurrency.objects.create(name='ABAN', price=Decimal('5.00'))

    def test_create_order_success(self):
        order = OrderService.create(user=self.wallet.user, crypto=self.crypto, amount=Decimal('10.00'))
        self.wallet.refresh_from_db()
        self.assertEqual(self.wallet.balance, Decimal('50.00'))  # 50 left after buying 10 ABAN (5*10=50)
        self.assertEqual(order.amount, Decimal('10.00'))
        self.assertEqual(order.total_price, Decimal('50.00'))
        self.assertEqual(order.state, 'PENDING')

    def test_create_order_insufficient_balance(self):
        with self.assertRaises(ValueError):
            OrderService.create(user=self.wallet.user, crypto=self.crypto, amount=Decimal('50.00'))

    def test_order_processing_below_threshold(self):
        order = OrderService.create(user=self.wallet.user, crypto=self.crypto, amount=Decimal('1.00'))
        self.assertTrue(order.is_aggregated)

    def test_order_processing_above_threshold(self):
        order = OrderService.create(user=self.wallet.user, crypto=self.crypto, amount=Decimal('10.00'))
        self.assertFalse(order.is_aggregated)
