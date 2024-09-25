import logging

from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from commons.messages.error_messages import ErrorMessages
from commons.messages.log_messges import LogMessages

logger = logging.getLogger(__name__)
User = get_user_model()


class BaseAuthSerializer(serializers.Serializer):
    access_token = serializers.CharField(read_only=True)
    refresh_token = serializers.CharField(read_only=True)

    def generate_tokens(self, user):
        refresh_token = TokenObtainPairSerializer.get_token(user)
        return {
            "access_token": str(refresh_token.access_token),
            "refresh_token": str(refresh_token)
        }


class RegisterSerializer(BaseAuthSerializer):
    username = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    def validate(self, attrs):
        username = attrs.get("username")

        if User.objects.filter(username=username).exists():
            logger.warning(LogMessages.register_existing_user(username))
            raise ValidationError(
                detail=ErrorMessages.REGISTRATION_FAILED.message, code=ErrorMessages.REGISTRATION_FAILED.code
            )
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
        )
        return self.generate_tokens(user)


class LoginSerializer(BaseAuthSerializer):
    username = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        user = authenticate(username=username, password=password)
        if not user:
            raise ValidationError(
                detail=ErrorMessages.INVALID_CREDENTIALS.message, code=ErrorMessages.INVALID_CREDENTIALS.code
            )

        attrs["user"] = user
        return attrs

    def create(self, validated_data):
        user = validated_data["user"]
        return self.generate_tokens(user)
