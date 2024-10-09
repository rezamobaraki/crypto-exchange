from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from accounts.models import Wallet
from commons.models import BaseModel
from transactions.enums import TransactionTypes


class Transaction(BaseModel):
    wallet = models.ForeignKey(Wallet, on_delete=models.DO_NOTHING, related_name="transactions")
    type = models.CharField(max_length=20, choices=TransactionTypes.choices)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]
