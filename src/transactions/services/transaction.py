from django.db import transaction

from transactions.enums import TransactionTypes
from transactions.models.transaction import Transaction


class TransactionService:
    repository = Transaction

    @transaction.atomic
    def wallet_withdraw(self, *, wallet_id, amount, order_id) -> int:
        return self.repository.objects.create(
            wallet_id=wallet_id, amount=amount, order_id=order_id, type=TransactionTypes.WITHDRAWAL
        )

    @transaction.atomic
    def wallet_deposit(self, *, wallet_id, amount) -> int:
        return self.repository.objects.create(wallet_id=wallet_id, amount=amount, type=TransactionTypes.DEPOSIT)
