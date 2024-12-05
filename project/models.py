import uuid
from datetime import timedelta

from django.contrib.auth.models import AbstractBaseUser, AbstractUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.timezone import now


class CustomUserManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError("The phone number must be provided")

        user = self.model(phone=phone, **extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if not extra_fields.get("is_staff"):
            raise ValueError("Superuser must have is_staff=True.")
        if not extra_fields.get("is_superuser"):
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(phone, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=20, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone


class OTP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="otp")
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        return now() > self.created_at + timedelta(minutes=5)

    def __str__(self):
        return f"OTP for {self.user.phone}"


class Clinic(models.Model):
    name = models.CharField(max_length=128)

    longitude = models.CharField(max_length=256)
    latitude = models.CharField(max_length=256)

    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self) -> str:
        return self.name


class Doctor(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    image = models.ImageField(upload_to="doctor-images/")
    phone = models.CharField(max_length=15)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return super().__str__()

    def get_full_name(self):
        return self.first_name + " " + self.last_name


class ClinicImage(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="clinic-images/")

    def __str__(self) -> str:
        return str(self.clinic)


class ServiceType(models.Model):
    name = models.CharField(max_length=128)
    color = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.color


class Service(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    type = models.ForeignKey(ServiceType, on_delete=models.SET_NULL, null=True)
    doctors = models.ManyToManyField(Doctor, blank=True)

    def __str__(self) -> str:
        return f"{self.type.name} - {self.clinic.name}"
