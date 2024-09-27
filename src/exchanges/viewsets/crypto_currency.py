from rest_framework import permissions

from commons.pagination import StandardResultsSetPagination
from commons.viewsets import ListModelViewSet
from exchanges.models.crypto_currency import CryptoCurrency
from exchanges.serializers.crypto_currency import CryptoCurrencySerializer


class CryptoCurrencyViewSet(ListModelViewSet):
    queryset = CryptoCurrency.objects.all()
    serializer_class = CryptoCurrencySerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [permissions.AllowAny]
