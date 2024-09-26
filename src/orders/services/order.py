from decimal import Decimal

from django.conf import settings
from django.db import transaction

from accounts.services.wallet import WalletService
from orders.enums import OrderStates
from orders.models.order import Order
from orders.tasks import process_aggregate_orders, process_large_order
from transactions.services.transaction import TransactionService

AGGREGATION_THRESHOLD = settings.ORDER_AGGREGATION_THRESHOLD


class OrderService:
    wallet_service = WalletService()
    transaction_service = TransactionService()

    @classmethod
    def check(cls, *, wallet, coin, amount):
        total_price = coin.price * amount
        return cls.wallet_service.check_balance(wallet=wallet, amount=total_price)

    @classmethod
    @transaction.atomic
    def create(cls, *, wallet_id, crypto, amount):
        total_price = crypto.price * Decimal(amount)
        cls.wallet_service.withdraw(wallet_id=wallet_id, value=total_price, order_id=None)
        order = Order.objects.create(
            wallet_id=wallet_id, crypto=crypto, amount=amount,
            total_price=total_price, state=OrderStates.PENDING
        )
        cls.transaction_service.wallet_withdraw(wallet_id=wallet_id, amount=total_price, order_id=order.id)
        cls.process(order=order, crypto_id=crypto.id, crypto_name=crypto.name, amount=amount, total_price=total_price)
        return order

    @staticmethod
    def process(order, crypto_id, crypto_name, amount, total_price):
        if order.total_price < AGGREGATION_THRESHOLD:
            process_aggregate_orders.delay(
                order_id=order.id, crypto_id=crypto_id, crypto_name=crypto_name,
                amount=amount, total_price=total_price
            )
            order.is_aggregated = True
            order.save()
        else:
            process_large_order.delay(order_id=order.id)
