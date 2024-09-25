from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import include, path

from commons.views import health_check

urlpatterns = [
                  path("health/", health_check, name="health-check"),
                  path("api/v1/", include("routers.urls")),
                  path('admin/', admin.site.urls),
              ] + debug_toolbar_urls()
