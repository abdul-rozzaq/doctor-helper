from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .routers import router
from .views import SendOTPView, VerifyOTPView

app_name = "project"

urlpatterns = [
    path("", include(router.urls)),
    path("send-otp/", SendOTPView.as_view()),
    path("verify-otp/", VerifyOTPView.as_view()),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("verify/", TokenVerifyView.as_view(), name="token_verify"),
]
