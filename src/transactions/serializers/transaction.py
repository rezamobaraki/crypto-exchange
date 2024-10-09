from rest_framework import serializers
from transactions.models.transaction import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ("id", "wallet", "amount", "content_type", "object_id", "type")
        read_only_fields = fields
