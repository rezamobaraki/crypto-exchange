from rest_framework.routers import SimpleRouter

from accounts.viewsets.authentication import LoginViewSet, RegisterViewsSet

app_name = 'authentication'

router = SimpleRouter()

router.register(r'login', LoginViewSet, basename='login')
router.register(r'register', RegisterViewsSet, basename='register')

urlpatterns = router.urls
