from django import forms
from users.models import Address


class CheckoutForm(forms.Form):
    billing_address = forms.IntegerField(required=True)
