from django.urls import path
from . import views


urlpatterns = [
    path("valuta/", views.get_valuta, name="get_valuta"),
]