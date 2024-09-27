from django.core.exceptions import ValidationError
from rest_framework import serializers

from commons.messages.error_messages import ErrorMessages
from exchanges.models.crypto_currency import CryptoCurrency
from orders.models.order import Order
from orders.services.order import OrderService


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    crypto = serializers.SlugRelatedField(slug_field='name', queryset=CryptoCurrency.objects.all())

    class Meta:
        model = Order
        fields = ("id", "user", "crypto", "amount", "total_price")
        read_only_fields = ("id", "total_price")

    def validate(self, attrs):
        if not OrderService.check(user=attrs["user"], crypto=attrs["crypto"], amount=attrs["amount"]):
            raise ValidationError(
                message=ErrorMessages.INSUFFICIENT_BALANCE.message, code=ErrorMessages.INSUFFICIENT_BALANCE.code
            )
        return attrs

    def create(self, validated_data):
        return OrderService.create(
            user=validated_data["user"], crypto=validated_data["crypto"], amount=validated_data["amount"]
        )
