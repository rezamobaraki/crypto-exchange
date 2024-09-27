from rest_framework import serializers

from transactions.models.transaction import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ("id", "wallet", "amount", "order_id", "type")
        read_only_fields = fields
