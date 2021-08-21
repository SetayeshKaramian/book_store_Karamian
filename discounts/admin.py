from django.contrib import admin
from .models import Coupon, Discount

# Register models.
admin.site.register(Coupon)
admin.site.register(Discount)
