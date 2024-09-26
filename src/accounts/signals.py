from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


@receiver(post_save, sender=User)
def create_wallet(sender, instance, created, **kwargs):
    if created and not instance.wallet:
        from accounts.models import Wallet
        Wallet.objects.create(user=instance)
