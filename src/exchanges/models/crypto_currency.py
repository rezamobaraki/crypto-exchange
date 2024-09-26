from django.db import models

from commons.models import BaseModel


class CryptoCurrency(BaseModel):
    name = models.CharField(max_length=10, unique=True)


class CryptoPrice(models.Model):
    cryptocurrency = models.ForeignKey(CryptoCurrency, on_delete=models.SET_NULL, null=True, blank=True)
    crypto_name = models.CharField(max_length=10, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
