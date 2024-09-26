from decimal import Decimal

from rest_framework import serializers

from accounts.models import Wallet
from accounts.services.wallet import WalletService
from transactions.services.transaction import TransactionService


class WalletSerializer(serializers.ModelSerializer):
    balance = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Wallet
        fields = ("balance",)


class WalletDepositSerializer(WalletSerializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2, min_value=Decimal(0.0), write_only=True)

    class Meta(WalletSerializer.Meta):
        fields = WalletSerializer.Meta.fields + ("amount",)

    def update(self, instance, validated_data):
        WalletService.deposit(wallet_id=instance.id, value=validated_data["amount"])
        TransactionService.wallet_deposit(wallet_id=instance.id, amount=validated_data["amount"])
        instance.refresh_from_db()
        return instance
