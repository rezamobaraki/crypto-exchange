from rest_framework import routers

from exchanges.viewsets.crypto_currency import CryptoCurrencyViewSet

router = routers.SimpleRouter()

router.register("crypto-currency", CryptoCurrencyViewSet)

urlpatterns = router.urls
