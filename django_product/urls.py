from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import set_language
# from django.contrib.sitemaps.views import sitemap
# from .sitemaps import ProductSitemap, StaticSitemap, CategorySitemap, SubCategorySitemap, NewsSitemap
# from .views import robots_txt


# sitemaps = {
#     'product': ProductSitemap,
#     'category': CategorySitemap,
#     'subcategory': SubCategorySitemap,
#     'news': NewsSitemap,
#     'static': StaticSitemap,
# }


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
    # path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    # path('robots.txt', robots_txt, name='robots'),

    prefix_default_language = False
)

handler404 = "django_product.views.handler404"
handler500 = "django_product.views.handler500"


if settings.DEBUG:
    # import debug_toolbar
    # urlpatterns = [
    #     path('__debug__/', include(debug_toolbar.urls)),
    #     ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


