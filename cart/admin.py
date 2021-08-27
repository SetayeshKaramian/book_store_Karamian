from django.contrib import admin
from .models import OrderBook, Order, Book
from django.utils.safestring import mark_safe
from django.shortcuts import reverse


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ['user', 'coupon', 'ordered_date', 'paid', 'billing_address', 'view_order']
    list_filter = ['paid']
    search_fields = ['user', 'coupon', 'ordered_date', 'billing_address', ]

    @admin.display(description='اقلام')
    def view_order(self, order):
        url = reverse("admin:cart_orderbook_changelist")
        link = '<a href="%s">%s</a>' % (url + '?order=' + str(order.id), 'مشاهده اقلام')
        return mark_safe(link)


class OrderBookAdmin(admin.ModelAdmin):
    model = OrderBook
    list_display = ['book', 'd_order', 'quantity']
    search_fields = ['book__title']

    @admin.display(description='کد سفارش')
    def d_order(self, orderbook):
        return orderbook.order.id


# Register models.
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderBook, OrderBookAdmin)
