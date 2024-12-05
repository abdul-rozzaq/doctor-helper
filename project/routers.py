from rest_framework.routers import DefaultRouter

from .views import ClinicViewSet

router = DefaultRouter()

router.register("clinic", ClinicViewSet)
