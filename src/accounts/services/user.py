from django.contrib.auth import get_user_model
from django.db import transaction

from accounts.models import Wallet


class UserService:
    # TODO: wallet should inject as a dependency
    model = get_user_model()

    @classmethod
    @transaction.atomic
    def create_user_and_wallet(cls, *, username: str, password: str) -> model:
        user = cls.model.objects.create_user(username=username, password=password)
        Wallet.objects.create(user=user)
        return user
