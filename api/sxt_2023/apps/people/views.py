from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.base_user import BaseUserManager
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import PolymorphicProxySerializer, extend_schema
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin
from rest_framework.request import Request
from rest_framework.response import Response
# from wailer.models import Email  # Temporarily commented out

from sxt_2023.apps.sxt2023_api.models import Brand

from .serializers import (
    AnonUserSerializer,
    AuthRequest,
    AuthUserSerializer,
    UserSerializer,
)

User = get_user_model()


class MeViewSet(viewsets.GenericViewSet):
    """
    Basic ViewSet that handles login and loging of the user through the API
    using the session.
    """

    permission_classes = [permissions.AllowAny]
    serializer_class = AuthUserSerializer
    pagination_class = None

    def get_serializer_class(self):
        if self.action == "create":
            return AuthRequest
        else:
            return AuthUserSerializer

    @extend_schema(
        operation_id="get_current_user",
        responses=PolymorphicProxySerializer(
            component_name="User",
            resource_type_field_name="is_authenticated",
            serializers={
                "true": AuthUserSerializer,
                "false": AnonUserSerializer,
            },
            many=False,
        ),
    )
    def list(self, request: Request) -> Response:
        """
        Retrieves the user's current information, whether they are logged in or
        not.
        """

        if request.user.is_authenticated:
            data = AuthUserSerializer(
                instance=request.user,
                context=self.get_serializer_context(),
            ).data
        else:
            data = dict(is_authenticated=False)

        return Response(data)

    @extend_schema("login")
    def create(self, request: Request) -> Response:
        """
        Call this to login. It will implicitly logout if logged in already.
        """

        ser = self.get_serializer(data=request.data)
        ser.is_valid(raise_exception=True)

        if user := get_object_or_404(User, email=ser.data["email"]):
            login(request, user)

        return self.list(request)  # noqa

    @extend_schema("logout")
    @action(methods=["post"], detail=False)
    def logout(self, request: Request) -> Response:
        """
        Call this to logout. If already not connected then nothing happens.
        """

        if request.user.is_authenticated:
            logout(request)

        return self.list(request)  # noqa


class Register(viewsets.GenericViewSet, CreateModelMixin):
    permission_classes = [permissions.AllowAny]
    # authentication_classes = []  # TMP
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if not Brand.objects.filter(pk=request.data["registration_brand"]).exists():
            return Response(status=400, data="BRAND_NOT_FOUND")

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        email = BaseUserManager.normalize_email(request.data["email"])
        brand = Brand.objects.filter(pk=request.data["registration_brand"]).first()

        # TODO: Uncomment when email system is configured
        # Email.send(
        #     "registration",
        #     dict(
        #         brand=brand.name,
        #         address=brand.postal_address,
        #         email=email,
        #         locale="es",
        #     ),
        # )

        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
