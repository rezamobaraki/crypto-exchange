from decimal import Decimal

from celery import shared_task
from django.conf import settings
from django.db import transaction
from django.db.models import Sum

from core.settings.third_parties.redis_templates import RedisNameTemplates
from exchanges.services.exchange_integration import ExchangeService
from orders.enums import OrderStates
from orders.models.order import Order

RedisClient = settings.REDIS
AGGREGATION_THRESHOLD = settings.ORDER_AGGREGATION_THRESHOLD

# it can consider as retrying the task if it fails
@shared_task
def process_aggregate_orders(*, order_id, crypto_name, new_total_price):
    # TODO(Refactor) : it should broken down into smaller functions for better readability and maintainability (SRP)
    """
    This function processes aggregate orders using Redis Lock to handle concurrency and Redis Pipeline to ensure atomicity of the Redis operations.

    Assumption: I assume that Only one worker always handles the orders. or I can use Redis Locks to handle the concurrency issues.
    Persistent: Use AOF (Append Only File) for persistence during application crashes.
    Update:
        - Redis Locks (Distributed Locking): 	Single command per request
                Use Redis Locks to ensure that only one worker modifies the order aggregation data at a time.
                This approach will give you the strongest guarantee that no race conditions or concurrent updates occur.
          ```
          if lock.acquire(blocking=True):
                # Critical Section
                # Modify the order aggregation data
            lock.release()
          ```
        - Redis Pipeline for Optimize multiple command execution
            ```
             with RedisClient.pipeline() as pipe:
                # Start the transaction
            pipe.execute()
            ```
        - Using Redis WATCH for Optimistic Locking

    """

    redis_name = RedisNameTemplates.aggregate_orders(crypto_name=crypto_name)
    RedisClient.hincrbyfloat(redis_name, "total_price", float(new_total_price))
    RedisClient.rpush(f"{redis_name}:order_ids", order_id)

    new_total_price = Decimal(RedisClient.hget(redis_name, "total_price") or 0)
    if new_total_price >= AGGREGATION_THRESHOLD:
        order_ids = RedisClient.lrange(f"{redis_name}:order_ids", 0, -1)

        with transaction.atomic():
            ExchangeService.buy_from_exchange(crypto_name=crypto_name, amount=new_total_price)
            Order.objects.filter(id__in=order_ids).update(state=OrderStates.COMPLETED)

        RedisClient.delete(redis_name)
        RedisClient.delete(f"{redis_name}:order_ids")


@shared_task
def process_large_order(order_id):
    with transaction.atomic():
        order = Order.objects.select_for_update().filter(id=order_id).first()
        ExchangeService.buy_from_exchange(crypto_name=order.crypto.name, amount=order.total_price)
        order.state = OrderStates.COMPLETED
        order.save()


@shared_task
def periodical_aggregated_orders_check_redis():
    """
    This task will periodically check for aggregated orders and process them if the total price is greater than or equal to the threshold.
    if the total price is greater than or equal to the threshold, it will buy the crypto from the exchange and update the state of the orders to COMPLETED.
    """
    crypto_names = RedisClient.keys(RedisNameTemplates.aggregate_orders(crypto_name='*'))
    for redis_name in crypto_names:
        total_price = Decimal(RedisClient.hget(redis_name, "total_price") or 0)
        if total_price >= AGGREGATION_THRESHOLD:
            order_ids = RedisClient.lrange(f"{redis_name}:order_ids", 0, -1)

            with transaction.atomic():
                crypto_name = redis_name.split(':')[-1]
                ExchangeService.buy_from_exchange(crypto_name=crypto_name, amount=total_price)
                Order.objects.filter(id__in=order_ids).update(state=OrderStates.COMPLETED)

            RedisClient.delete(redis_name)
            RedisClient.delete(f"{redis_name}:order_ids")


@shared_task
def periodical_aggregated_orders_check_db():
    """
    This task will periodically check for aggregated orders and process them if the total price is greater than or equal to the threshold.
    If the total price is greater than or equal to the threshold, it will buy the crypto from the exchange and update the state of the orders to COMPLETED.
    If the total price is below the threshold, it will call process_aggregate_orders for each order.
    """
    grouped_orders = (
        Order.objects.filter(is_aggregated=True, state=OrderStates.PENDING)
        .select_related('crypto')
        .values('crypto__name')
        .annotate(total_price=Sum('total_price'))
    )
    for group in grouped_orders:
        crypto_name, total_price = group['crypto__name'], group['total_price']

        if total_price >= AGGREGATION_THRESHOLD:
            with transaction.atomic():
                individual_orders = Order.objects.filter(
                    is_aggregated=True, state=OrderStates.PENDING, crypto__name=crypto_name
                )
                ExchangeService.buy_from_exchange(crypto_name=crypto_name, amount=total_price)
                individual_orders.update(state=OrderStates.COMPLETED)
        else:
            individual_orders = Order.objects.filter(
                is_aggregated=True, state=OrderStates.PENDING, crypto__name=crypto_name
            ).select_related('crypto')
            for order in individual_orders:
                process_aggregate_orders.delay(
                    order_id=order.id,
                    crypto_name=order.crypto.name,
                    amount=order.amount,
                    new_total_price=order.total_price
                )
