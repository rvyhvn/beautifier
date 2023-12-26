from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from .views import AppView

urlpatterns = [
    path("", AppView.as_view(), name="app"),
    path("products/", include("products.urls")),
    # TODO: add more applications url when it's already configured.
    path("admin/", admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
