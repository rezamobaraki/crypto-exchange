from commons.pagination import StandardResultsSetPagination
from commons.viewsets import CreateRetrieveListModelViewSet
from orders.models.order import Order
from orders.serializers.order import OrderSerializer


class OrderViewSet(CreateRetrieveListModelViewSet):
    """
     we can use
        - RouterRateLimiter: count all requests
        - UserRateLimiter: count requests per user
        - FraudDetection: prevent requests that come during a short period of time
    in order to prevent spamming and decrease the load on the server
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return Order.objects.filter(wallet_id=self.request.user.wallet.id)
