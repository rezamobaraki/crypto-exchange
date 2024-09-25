from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from accounts.models import Wallet
from accounts.serializers.wallet import WalletDepositSerializer, WalletSerializer
from commons.viewsets import RetrieveUpdateModelViewSet


class WalletViewSet(RetrieveUpdateModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.wallet

    def get_serializer_class(self):
        if self.action == 'deposit':
            return WalletDepositSerializer
        return super().get_serializer_class()

    @action(detail=True, methods=["patch"], url_path="deposit", serializer_class=WalletDepositSerializer)
    def deposit(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
