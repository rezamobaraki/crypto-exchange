import factory
from factory.django import DjangoModelFactory

from exchanges.models.crypto_currency import CryptoCurrency


class CryptoCurrencyFactory(DjangoModelFactory):
    class Meta:
        model = CryptoCurrency

    name = factory.Faker('lexify', text='????')
    price = factory.Faker('random_int', min=1, max=10000)
