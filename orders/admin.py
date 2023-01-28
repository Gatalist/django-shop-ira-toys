from django.contrib import admin
from .models import Status, ProductInOrder, Order


class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0


class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0
    readonly_fields = ("product", "nmb", "price_per_item", "total_price",)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_active", "created", "updated")
    list_display_links = ("name",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "status", "total_price", "lastname", "firstname", "created")
    list_display_links = ("status",)

    inlines = [ProductInOrderInline, ]
