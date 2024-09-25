from django.urls import path

from accounts.viewsets.wallet import WalletViewSet

app_name = 'wallet'

urlpatterns = [
    path('', WalletViewSet.as_view({'get': 'retrieve'}), name='wallet-detail'),
    path('deposit/', WalletViewSet.as_view({'patch': 'deposit'}), name='wallet-deposit'),

]
