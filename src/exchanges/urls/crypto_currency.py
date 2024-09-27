from rest_framework import routers

from exchanges.viewsets.crypto_currency import CryptoCurrencyViewSet

app_name = 'crypto-currency'

router = routers.SimpleRouter()

router.register("", CryptoCurrencyViewSet)

urlpatterns = router.urls
