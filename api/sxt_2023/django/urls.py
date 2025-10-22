from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.utils.translation import gettext_lazy as _
from rest_framework.routers import DefaultRouter, SimpleRouter

from sxt_2023.apps.people.views import MeViewSet, Register
from sxt_2023.apps.sxt2023_api.views import (
    BrandsViewset,
    get_brand_info,
    get_brands_info,
    visit_tree,
)

admin.site.site_title = _("SXT 2023")
admin.site.site_header = _("SXT 2023")


if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("user/me", MeViewSet, basename="user_me")
router.register("user/registration", Register, basename="user_registration")

urlpatterns = [
    path("back/admin/", admin.site.urls),
    path("back/api/", include(router.urls)),
    path("back/api/brands/", get_brands_info, name="get_brands_info"),
    path("back/api/brands/visit/<tree_id>/", visit_tree, name="visit_tree"),
    path("back/api/brands/<pk>/", BrandsViewset.as_view({"get": "retrieve"})),
    path("back/api/brands/tree/<tree_id>/", get_brand_info, name="get_brand_info"),
    # path("back/api/wailer/", include("wailer.urls")),  # Temporarily commented out
]

if settings.DEBUG:
    from drf_spectacular.views import (
        SpectacularAPIView,
        SpectacularRedocView,
        SpectacularSwaggerView,
    )

    urlpatterns = [
        path(
            "back/api/schema/",
            SpectacularAPIView.as_view(),
            name="schema",
        ),
        path(
            "back/api/schema/swagger-ui/",
            SpectacularSwaggerView.as_view(url_name="schema"),
            name="swagger-ui",
        ),
        path(
            "back/api/schema/redoc/",
            SpectacularRedocView.as_view(url_name="schema"),
            name="redoc",
        ),
    ] + urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
