from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import Brand, Visit

# Register your models here.


User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    list_per_page = 1000
    list_max_show_all = 10000
    list_display = ("email", "registration_brand", "visits_count", "date_joined")
    list_filter = ("registration_brand", "date_joined")
    list_select_related = ["registration_brand"]


class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "postal_address", "registration_url", "tree_url", "total_users", "total_visits")


class VisitAdmin(admin.ModelAdmin):
    list_per_page = 1000
    list_max_show_all = 10000
    list_display = ("user", "brand", "visited_at")
    list_filter = ("brand", "visited_at") 


admin.site.register(User, UserAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Visit, VisitAdmin)
