from django.contrib import admin
from .models import Coupon, DiscountPercent, DiscountUpTo

# Register models.
admin.site.register(Coupon)
admin.site.register(DiscountPercent)
admin.site.register(DiscountUpTo)
