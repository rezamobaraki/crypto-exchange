from rest_framework.routers import SimpleRouter

from orders.viewsets.order import OrderViewSet

router = SimpleRouter()
router.register("", OrderViewSet)

urlpatterns = router.urls
