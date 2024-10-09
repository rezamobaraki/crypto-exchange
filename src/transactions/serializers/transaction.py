from rest_framework import serializers

from transactions.models.transaction import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    content_type_name = serializers.SerializerMethodField()

    class Meta:
        model = Transaction
        fields = ("id", "wallet", "amount", "content_type", "content_type_name", "object_id", "type")
        read_only_fields = fields

    def get_content_type_name(self, obj):
        return obj.content_type.model
