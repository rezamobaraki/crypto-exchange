from django.db import models

from commons.models import BaseModel


class CryptoCurrency(BaseModel):
    name = models.CharField(max_length=10, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)


"""
We can have a model to store the price of a cryptocurrency. This model will have a foreign key to the CryptoCurrency model.

class CryptoPrice(BaseModel):
    
    # TODO: consider an approach to update price in real-time
    
    cryptocurrency = models.ForeignKey(CryptoCurrency, on_delete=models.SET_NULL, null=True, blank=True)
    crypto_name = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
"""
