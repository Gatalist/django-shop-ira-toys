from django.contrib import admin
from .models import Contact, Mailing
from .tasks import send_mailing_all


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "date")
    list_display_links = ("email",)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "date", "is_active",)
    list_display_links = ("title",)

    def save_model(self, obj):
        obj.save()
        tast = obj.id
        return send_mailing_all.delay(tast)
