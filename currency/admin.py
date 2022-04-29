from django.contrib import admin
from .models import Usd, Eur, Uah


@admin.register(Usd)
class UsdAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "date")
    list_display_links = ("name",)


@admin.register(Eur)
class EurAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "date")
    list_display_links = ("name",)


# @admin.register(Uah)
# class UahAdmin(admin.ModelAdmin):
#     list_display = ("id", "name", "date")
#     list_display_links = ("name",)   