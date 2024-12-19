import random

from rest_framework import serializers

from project.utils import calculate_distance

from .models import Clinic, ClinicImage, Doctor, Service, ServiceType


class SendOTPSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=15)


class VerifyOTPSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=15)
    otp = serializers.CharField(max_length=6)


class ClinicImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicImage
        fields = "__all__"


class ClinicSerializer(serializers.ModelSerializer):
    images = ClinicImageSerializer(many=True)
    rate = serializers.SerializerMethodField()

    class Meta:
        model = Clinic
        fields = "__all__"

    def __init__(self, instance=None, data=..., **kwargs):
        super().__init__(instance, data, **kwargs)

        self.latitude = self.context["request"].GET.get("latitude")
        self.longitude = self.context["request"].GET.get("longitude")

    def get_rate(self, instance):
        return float(random.randint(20, 50) / 10)

    def to_representation(self, instance):
        response = super().to_representation(instance)

        if self.latitude and self.longitude:
            response["distance"] = calculate_distance(float(instance.latitude), float(instance.longitude), float(self.latitude), float(self.longitude))
            response["distance"] = round(response["distance"] * 10) / 10

        return response


class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"


class CalcDistanceSerializer(serializers.Serializer):
    longitude = serializers.FloatField()
    latitude = serializers.FloatField()
