from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("project.urls", namespace="v1")),
    path("auth/", include("rest_framework.urls")),
]
