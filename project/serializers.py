from rest_framework import serializers

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

    class Meta:
        model = Clinic
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"
