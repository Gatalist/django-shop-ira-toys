from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import set_language
# from django.conf.urls import handler404, handler500


urlpatterns = [
    # path('pages/', include('django.contrib.flatpages.urls')),
    # path('rosetta/',include('rosetta.urls')),

] + i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path("set_language/<str:language>/", set_language, name="set-language"),

    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path("contact/", include("contact.urls")),
    path("orders/", include("orders.urls")),
    path("currency/", include("currency.urls")),
    path("", include("products.urls")),

    prefix_default_language = False
)

handler404 = "django_product.views.error_404"
handler500 = "django_product.views.error_500"


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


