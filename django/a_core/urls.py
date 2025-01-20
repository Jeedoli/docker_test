from a_apis.api.image import router
from a_apis.views import image_upload_view
from ninja import NinjaAPI

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

api = NinjaAPI()
api.add_router("/images/", router)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
    path("", image_upload_view, name="image_upload"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
