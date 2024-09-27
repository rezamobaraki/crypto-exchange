import factory
from factory import faker

from accounts.models import Wallet


class WalletFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Wallet

    balance = faker.Faker('random_int', min=0, max=1000)
