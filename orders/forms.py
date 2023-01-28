from django import forms


class OrderForm(forms.Form):
    """Форма отзыва"""
    firstname = forms.CharField(required=True)
    lastname = forms.CharField(required=True)
    email = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    city = forms.CharField(required=True)
