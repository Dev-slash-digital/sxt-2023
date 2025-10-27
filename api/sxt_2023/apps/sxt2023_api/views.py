from django.contrib.auth import get_user_model
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets
# from wailer.models import Email  # Temporarily commented out

from .models import Brand, Visit
from .serializers import BrandSerializer

User = get_user_model()


class BrandsViewset(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()


def get_brands_info(request):
    brands = Brand.objects.values("name", "slug", "postal_address", "maps_link")

    # Check what user has visited
    visits = []
    if request.user and request.user.is_authenticated:
        visits = list(request.user.visit_set.values("brand__slug"))

    visited = [x["brand__slug"] for x in visits]
    for brand in brands:
        brand["visited"] = brand["slug"] in visited

    return JsonResponse(list(brands), safe=False)


def visit_tree(request, tree_id):
    brand = get_object_or_404(Brand, tree_id=tree_id)

    # Save visit to DB
    if request.user and request.user.is_authenticated:
        _, created = Visit.objects.get_or_create(
            user=request.user,
            brand=brand,
        )

        if created:
            visits_count = request.user.visits_count

            # On seventh visit, send the "raffle" email
            if visits_count == 7:
                # TODO: Uncomment when email system is configured
                # Email.send(
                #     "raffleconfirmation",
                #     dict(
                #         email=request.user.email,
                #         locale="es",
                #     ),
                # )
                pass

    return JsonResponse(model_to_dict(brand))


def get_brand_info(request, tree_id):
    brand = get_object_or_404(Brand, tree_id=tree_id)
    return JsonResponse(model_to_dict(brand))
