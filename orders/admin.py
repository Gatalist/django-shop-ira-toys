from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Status, ProductInBasket, ProductInOrder, Order

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
    

# @admin.register(ProductInOrder)
# class ProductInOrderAdmin(admin.ModelAdmin):
#     list_display = ("order", "product", "nmb", "price_per_item", "total_price", "created", "updated")
#     list_display_links = ("product",)
#     # readonly_fields = ("order", "product", "price_per_item", "total_price",)


# @admin.register(ProductInBasket)
# class ProductInBasketAdmin(admin.ModelAdmin):
#     list_display = ("id", "session_key", "product", "nmb", "price_per_item", "total_price", "created", "updated")
#     list_display_links = ("session_key",)
#     readonly_fields = ("get_image", "session_key", "nmb", "price_per_item", "total_price", "order", "product", "poster")

#     def get_image(self, obj):
#         return mark_safe(f'<img src="{obj.poster.url}" width="50" height="auto">')

#     get_image.short_description = "Миниатюра"
