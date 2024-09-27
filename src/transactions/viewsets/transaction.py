from rest_framework.permissions import IsAuthenticated

from commons.pagination import StandardResultsSetPagination
from commons.viewsets import RetrieveListModelViewSet
from transactions.models.transaction import Transaction
from transactions.serializers.transaction import TransactionSerializer


class TransactionViewSet(RetrieveListModelViewSet):
    serializer_class = TransactionSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Transaction.objects.filter(wallet=self.request.user.wallet)
        return Transaction.objects.none()
