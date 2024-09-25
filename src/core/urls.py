from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from commons.views import health_check

urlpatterns = [
                  path("health/", health_check, name="health-check"),
                  path("api/v1/", include("routers.urls")),
                  path('admin/', admin.site.urls),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
