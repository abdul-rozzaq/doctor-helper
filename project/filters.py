import django_filters
from django.db.models import Q

from .models import Clinic
from .utils import calculate_distance


class ClinicFilter(django_filters.FilterSet):
    latitude = django_filters.NumberFilter(method="filter_by_distance")
    longitude = django_filters.NumberFilter(method="filter_by_distance")
    radius = django_filters.NumberFilter(method="filter_by_distance")

    class Meta:
        model = Clinic
        fields = ["latitude", "longitude", "radius"]

    def filter_by_distance(self, queryset, name, value):
        longitude = self.data.get("longitude")
        latitude = self.data.get("latitude")
        radius = self.data.get("radius") or -1

        if not longitude or not latitude:
            return queryset

        try:
            longitude = float(longitude)
            latitude = float(latitude)
            radius = float(radius)
        except ValueError:
            return queryset.none()

        filtered_ids = []

        for clinic in queryset:
            if radius == -1 or calculate_distance(float(clinic.latitude), float(clinic.longitude), latitude, longitude) <= radius:
                filtered_ids.append(clinic.id)

        return queryset.filter(id__in=filtered_ids)
