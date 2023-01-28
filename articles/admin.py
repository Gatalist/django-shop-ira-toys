from django.contrib import admin
from .models import UpdateStatusPrduct, UpdateStatusView
from .tasks import update_status


@admin.register(UpdateStatusPrduct)
class UpdateStatusPrductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "upload", "date",)
    list_display_links = ("title",)
    # readonly_fields = ("title", "upload", "date")

    def save_model(self, request, obj, form, change):
        obj.save()
        task = obj.id
        return update_status.delay(task)


@admin.register(UpdateStatusView)
class UpdateStatusViewAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "status", "date",)
    list_display_links = ("title",)
    readonly_fields = ("title", "status", "date", "description")
