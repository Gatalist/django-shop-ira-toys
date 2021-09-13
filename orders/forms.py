from django import forms

from .models import Order


# class OrderForm(forms.ModelForm):
#     """Форма отзыва"""
#     class Meta:
#         model = Order
#         fields = ("firstname", "lastname", "email", "comment", "phone", "address")

class OrderForm(forms.Form):
    """Форма отзыва"""
    firstname = forms.CharField(required=True)
    lastname = forms.CharField(required=True)
    email = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    city = forms.CharField(required=True)