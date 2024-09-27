from decimal import Decimal

from django.test import override_settings, TestCase

from accounts.models import Wallet
from accounts.services.wallet import WalletService


@override_settings(DJANGO_SETTINGS_MODULE='core.settings.django.test')
class WalletServiceTestCase(TestCase):

    def setUp(self):
        self.wallet = Wallet.objects.create(balance=Decimal('100.00'))

    def test_deposit(self):
        WalletService.deposit(wallet_id=self.wallet.id, value=Decimal('50.00'))
        self.wallet.refresh_from_db()
        self.assertEqual(self.wallet.balance, Decimal('150.00'))

    def test_withdraw_success(self):
        WalletService.withdraw(wallet_id=self.wallet.id, value=Decimal('40.00'))
        self.wallet.refresh_from_db()
        self.assertEqual(self.wallet.balance, Decimal('60.00'))

    def test_withdraw_insufficient_balance(self):
        with self.assertRaises(ValueError):
            WalletService.withdraw(wallet_id=self.wallet.id, value=Decimal('200.00'))

    def test_check_balance(self):
        self.assertTrue(WalletService.check_balance(wallet=self.wallet, amount=Decimal('100.00')))
        self.assertFalse(WalletService.check_balance(wallet=self.wallet, amount=Decimal('150.00')))
