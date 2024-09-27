from rest_framework import status

from accounts.serializers import LoginSerializer, RegisterSerializer
from commons.mixins import FixStatusMixin
from commons.throttles import LoginRateThrottle, RegisterRateThrottle
from commons.viewsets import CreateModelViewSet


class RegisterViewsSet(FixStatusMixin, CreateModelViewSet):
    fix_status = status.HTTP_200_OK
    authentication_classes = []
    permission_classes = []
    throttle_classes = [RegisterRateThrottle]
    serializer_class = RegisterSerializer


class LoginViewSet(FixStatusMixin, CreateModelViewSet):
    fix_status = status.HTTP_200_OK
    authentication_classes = []

    permission_classes = []
    throttle_classes = [LoginRateThrottle]
    serializer_class = LoginSerializer
