from django.contrib import admin
from .models import OrderBook, Order


# Register models.
admin.site.register(OrderBook)
admin.site.register(Order)
