from django.contrib.auth import get_user_model
from django.db import models

from commons.models import BaseModel

User = get_user_model()


class Wallet(BaseModel):
    """
    We could consider coin= models.ForeignKey(Coin, on_delete=models.DO_NOTHING) and unique_together=('user', 'coin')
    here in order to have a wallet for each coin. However, for the sake of simplicity, we will assume that
    each user has only one currency wallet.
    """
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    balance = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.user}'

    def check_balance(self, value: float) -> bool:
        return self.balance >= value
