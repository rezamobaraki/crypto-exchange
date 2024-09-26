from rest_framework import routers

from transactions.viewsets.transaction import TransactionViewSet

app_name = 'transaction'

router = routers.SimpleRouter()

router.register('', TransactionViewSet, basename='transaction')

urlpatterns = router.urls
