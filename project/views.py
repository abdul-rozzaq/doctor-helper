import random
from datetime import timedelta

from django.utils.timezone import now
from rest_framework import status, viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import OTP, Clinic, ClinicImage, User
from .permissons import IsAdminOrReadOnly
from .serializers import ClinicSerializer, SendOTPSerializer, VerifyOTPSerializer
from .utils import send_otp_code


class SendOTPView(GenericAPIView):
    serializer_class = SendOTPSerializer

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone = serializer.validated_data["phone"]

        user, created = User.objects.get_or_create(phone=phone)

        otp_code = str(random.randint(100000, 999999))

        otp, created = OTP.objects.update_or_create(user=user, defaults={"code": otp_code, "created_at": now()})

        send_otp_code(phone, otp_code)

        return Response({"detail": "OTP muvaffaqiyatli yuborildi."}, status=status.HTTP_200_OK)


class VerifyOTPView(GenericAPIView):
    serializer_class = VerifyOTPSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone, code = serializer.validated_data["phone"], serializer.validated_data["otp"]

        try:
            user = User.objects.get(phone=phone)
            otp = OTP.objects.get(user=user, code=code)
        except (User.DoesNotExist, OTP.DoesNotExist):
            return Response({"detail": "Telefon raqami yoki OTP kodi noto‘g‘ri."}, status=status.HTTP_400_BAD_REQUEST)

        if otp.is_expired():
            return Response({"detail": "OTP kodi muddati tugagan."}, status=status.HTTP_400_BAD_REQUEST)

        otp.delete()

        refresh = RefreshToken.for_user(user)

        return Response({"refresh": str(refresh), "access": str(refresh.access_token)}, status=status.HTTP_200_OK)


class ClinicViewSet(viewsets.ModelViewSet):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer
    permission_classes = [IsAdminOrReadOnly]
