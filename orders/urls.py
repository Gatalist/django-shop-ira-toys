from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path("basket_adding/", views.basket_adding, name="basket_adding"),
    path("checkout/", views.checkout, name="checkout"),
]