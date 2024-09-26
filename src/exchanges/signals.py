from django.db import transaction
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from exchanges.models.crypto_currency import CryptoCurrency, CryptoPrice


@receiver(pre_delete, sender=CryptoCurrency)
def set_crypto_name_on_delete(sender, instance, **kwargs):
    with transaction.atomic():
        CryptoPrice.objects.select_for_update().filter(cryptocurrency=instance).update(
            crypto_name=instance.name,
            cryptocurrency=None
        )
