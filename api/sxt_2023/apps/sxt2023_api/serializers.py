from rest_framework import serializers

from .models import Brand


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            "name",
            "slug",
            "postal_address",
            "maps_link",
            "tree_description",
        )
