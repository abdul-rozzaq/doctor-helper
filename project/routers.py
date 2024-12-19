from rest_framework.routers import DefaultRouter

from .views import ClinicViewSet, DoctorViewSet, ServiceViewSet

router = DefaultRouter()

router.register("clinic", ClinicViewSet)
router.register("service", ServiceViewSet)
router.register("doctor", DoctorViewSet)
