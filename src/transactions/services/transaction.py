from django.db import transaction

from transactions.enums import TransactionTypes
from transactions.models.transaction import Transaction


class TransactionService:
    repository = Transaction

    @classmethod
    @transaction.atomic
    def wallet_withdraw(cls, *, wallet_id, amount, order_id) -> int:
        return cls.repository.objects.create(
            wallet_id=wallet_id, amount=amount, order_id=order_id, type=TransactionTypes.WITHDRAWAL
        )

    @classmethod
    @transaction.atomic
    def wallet_deposit(cls, *, wallet_id, amount) -> int:
        return cls.repository.objects.create(wallet_id=wallet_id, amount=amount, type=TransactionTypes.DEPOSIT)
