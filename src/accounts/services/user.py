from django.contrib.auth import get_user_model
from django.db import transaction

from accounts.services.wallet import WalletService


class UserService:
    model = get_user_model()
    wallet_service = WalletService()

    @classmethod
    @transaction.atomic
    def create_user_with_wallet(cls, *, username: str, password: str) -> model:
        user = cls.model.objects.create_user(username=username, password=password)
        cls.wallet_service.create(user=user)
        return user
