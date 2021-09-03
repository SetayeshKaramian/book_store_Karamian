from django import forms
from users.models import Address
from .models import Order


class CheckoutForm(forms.Form):
    # shipping_address = forms.CharField(max_length=250)
    billing_address = forms.IntegerField(required=True)
    paid = forms.BooleanField(widget=forms.CheckboxInput())

    class Meta:
        model = Order
        fields = ('shipping_address', 'billing_address', 'paid')