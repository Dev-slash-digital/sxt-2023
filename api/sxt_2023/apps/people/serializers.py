from django.contrib.auth.base_user import BaseUserManager
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from sxt_2023.apps.sxt2023_api.models import Brand

from .models import User


class AuthUserSerializer(serializers.ModelSerializer):
    """
    Serializer used when the user is authenticated on /api/me/
    """

    class Meta:
        model = User
        fields = [
            "is_authenticated",
            "email",
            "visits_count",
        ]

    is_authenticated = serializers.BooleanField()


class AnonUserSerializer(serializers.Serializer):
    """
    The serializer used when the user is not authenticated (it's always
    returning the same thing but it's here for the OpenAPI spec).
    """

    class Meta:
        fields = [
            "is_authenticated",
        ]

    is_authenticated = serializers.BooleanField()

    def update(self, instance, validated_data):
        raise NotImplementedError

    def create(self, validated_data):
        raise NotImplementedError


class AuthRequest(serializers.Serializer):
    """
    Serializer to process requests to login
    """

    class Meta:
        fields = [
            "email",
            "password",
        ]

    email = serializers.EmailField()
    password = serializers.CharField(allow_blank=True)

    def update(self, instance, validated_data):
        raise NotImplementedError

    def create(self, validated_data):
        raise NotImplementedError


class UserSerializer(serializers.ModelSerializer):
    registration_brand = PrimaryKeyRelatedField(
        queryset=Brand.objects.all(),
    )

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "registration_brand",
            "visits_count",
        )

    def validate_email(self, value):
        normalized = BaseUserManager.normalize_email(value)

        if User.objects.filter(email=normalized).exists():
            raise serializers.ValidationError("EMAIL_TAKEN")

        return normalized
