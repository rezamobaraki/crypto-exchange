from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

app_name = "api-v1"

schema_view = get_schema_view(
    openapi.Info(
        title="Crypto Exchange APIs",
        default_version='v1',
        description="Crypto Exchange Platform with Django and DRF",
        contact=openapi.Contact(email="rezam578@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
swagger = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
urlpatterns = [
    path("accounts/", include("routers.accounts", namespace="accounts"), name="accounts"),
    path("exchanges/", include("routers.exchanges", namespace="exchanges"), name="exchanges"),
    path("orders/", include("routers.orders", namespace="orders"), name="orders"),
    path("transactions/", include("routers.transactions", namespace="transactions"), name="transactions"),
]

urlpatterns += swagger
