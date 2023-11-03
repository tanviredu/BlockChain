from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

## setting up path static path with static directory
urlpatterns = [
    path("admin/", admin.site.urls),
    path("apiV1/", include("status.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
