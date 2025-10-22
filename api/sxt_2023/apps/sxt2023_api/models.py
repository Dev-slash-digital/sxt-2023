import uuid

from django.conf import settings
from django.db import models

from sxt_2023.apps.people.models import User, UuidPkModel


class Brand(UuidPkModel, models.Model):
    name = models.CharField(max_length=256)
    slug = models.CharField(max_length=256, unique=True)  # Mostly used for logo path
    postal_address = models.CharField(max_length=256, null=True, blank=True)
    maps_link = models.URLField(null=True, blank=True)
    tree_id = models.UUIDField(primary_key=False, default=uuid.uuid4, unique=True)
    tree_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return "Brand: {}".format(self.name)

    @property
    def registration_url(self):
        return "{}/registration/{}".format(settings.BASE_URL, self.id)

    @property
    def tree_url(self):
        if self.slug == "sxt":
            return "(scanning is disabled for this brand)"

        return "{}/scan/{}".format(settings.BASE_URL, self.tree_id)
    
    @property
    def total_users(self):
        return self.user_set.count()
    
    @property
    def total_visits(self):
        if self.slug == "sxt":
            return "(scanning is disabled for this brand)"
        return self.visit_set.count()


class Visit(UuidPkModel, models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    visited_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["brand", "user"], name="one_visit_per_brand_and_user"
            )
        ]
