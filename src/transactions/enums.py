from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError


class TransactionTypes(TextChoices):
    DEPOSIT = 'DEPOSIT', _('Deposit')
    WITHDRAWAL = 'WITHDRAWAL', _('Withdrawal')

    @classmethod
    def validate_choice(cls, value: str):
        if value not in cls.values:
            raise ValidationError(_("invalid_transaction_type"), code="invalid_transaction_type")
