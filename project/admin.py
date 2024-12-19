from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import OTP, Clinic, ClinicImage, Doctor, Service, ServiceType, User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("id", "first_name", "last_name", "phone", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("first_name", "last_name", "phone", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login",)}),
    )
    add_fieldsets = ((None, {"classes": ("wide",), "fields": ("first_name", "last_name", "phone", "password1", "password2", "is_staff", "is_active")}),)
    search_fields = ("phone",)
    ordering = ("phone",)


@admin.register(OTP)
class OTPAdmin(admin.ModelAdmin):
    list_display = ("user", "code", "created_at")
    search_fields = ("user__phone", "code")
    list_filter = ("created_at",)


class CLinicImageInline(admin.TabularInline):
    model = ClinicImage


@admin.register(Clinic)
class ClinicAdmin(admin.ModelAdmin):
    list_display = ["name", "longitude", "latitude", "opening_time", "closing_time"]
    inlines = [CLinicImageInline]


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "phone", "clinic"]
