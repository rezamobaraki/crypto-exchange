from django.db import models

from accounts.models import Wallet
from commons.models import BaseModel
from transactions.enums import TransactionTypes


class Transaction(BaseModel):
    wallet = models.ForeignKey(Wallet, on_delete=models.DO_NOTHING, related_name="transactions")
    type = models.CharField(max_length=20, choices=TransactionTypes.choices)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_id = models.IntegerField(null=True, blank=True)
