from django.urls import include, path

from .routers import router
from .views import SendOTPView, VerifyOTPView

app_name = "project"

urlpatterns = [
    path("", include(router.urls)),
    path("send-otp/", SendOTPView.as_view()),
    path("verify-otp/", VerifyOTPView.as_view()),
]
