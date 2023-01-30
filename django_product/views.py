from django_product.settings import LANGUAGES
from django.urls.base import resolve, reverse
from django.utils import translation
from urllib.parse import urlparse
from django.urls.exceptions import Resolver404
from django.http import HttpResponseRedirect
from django.shortcuts import render

# from django.views.generic import TemplateView
# from django.http import HttpResponse
# from django.views.decorators.http import require_GET
# from site_management.models import RobotsTxt


def set_language(request, language):
    for lang, _ in LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
    else:
        response = HttpResponseRedirect("/")
    return response


def handler404(request, exception):
    return render(request, 'errors/404.html', status=404)


def handler500(request):
    return render(request, "errors/500.html", status=500)


# @require_GET
# def robots_txt(request):
#     robots = RobotsTxt.objects.latest("id").text
#     return HttpResponse(robots, content_type="text/plain")