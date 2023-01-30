from django.contrib import admin
from .models import Usd


@admin.register(Usd)
class UsdAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "date")
    list_display_links = ("name",)

    # def has_add_permission(self, request):
    #     return False
