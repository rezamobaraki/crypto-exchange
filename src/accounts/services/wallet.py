from django.db import transaction
from django.db.models import F

from accounts.models import Wallet
from commons.messages.error_messages import ErrorMessages


class WalletService:
    model = Wallet

    @classmethod
    @transaction.atomic
    def deposit(cls, *, wallet_id: int, value: float) -> Wallet:
        return cls.model.objects.select_for_update().filter(id=wallet_id).update(balance=F('balance') + value)

    @classmethod
    @transaction.atomic
    def withdraw(cls, *, wallet_id: int, value: float) -> None:
        wallet = cls.model.objects.select_for_update().filter(id=wallet_id).first()
        if not wallet.check_balance(value):
            raise ValueError(ErrorMessages.INSUFFICIENT_BALANCE.message)
        wallet.balance = F('balance') - value
        wallet.save(update_fields=['balance'])
