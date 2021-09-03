from django.contrib import admin
from .models import Coupon, Discount


class CouponAdmin(admin.ModelAdmin):
    model = Coupon
    list_display = ['code', 'percentage', 'max_amount', 'flat_fee']
    list_filter = ['percentage', 'max_amount', 'flat_fee']
    search_fields = ['code']


class DiscountAdmin(admin.ModelAdmin):
    model = Discount
    list_display = ['title', 'percentage', 'flat_amount']
    list_filter = ['percentage', 'flat_amount']
    search_fields = ['title']


# Register models.
admin.site.register(Coupon, CouponAdmin)
admin.site.register(Discount, DiscountAdmin)
