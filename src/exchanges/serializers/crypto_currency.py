from rest_framework import serializers

from exchanges.models.crypto_currency import CryptoCurrency


class CryptoCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoCurrency
        fields = ["id", "name", "price"]
        read_only_fields = ["id", "name", "price"]
