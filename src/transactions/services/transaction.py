from django.contrib.contenttypes.models import ContentType
from django.db import transaction

from accounts.models import Wallet
from transactions.enums import TransactionTypes
from transactions.models.transaction import Transaction


class TransactionService:
    repository = Transaction

    @classmethod
    @transaction.atomic
    def wallet_withdraw(cls, *, wallet_id, amount, related_object):
        content_type = ContentType.objects.get_for_model(related_object)
        return cls.repository.objects.create(
            wallet_id=wallet_id,
            amount=amount,
            content_type=content_type,
            object_id=related_object.id,
            type=TransactionTypes.WITHDRAWAL
        )

    @classmethod
    @transaction.atomic
    def wallet_deposit(cls, *, wallet_id, amount):
        content_type = ContentType.objects.get_for_model(Wallet)
        return cls.repository.objects.create(
            wallet_id=wallet_id,
            amount=amount,
            content_type=content_type,
            object_id=wallet_id,
            type=TransactionTypes.DEPOSIT
        )
