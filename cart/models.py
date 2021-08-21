from book.models import Book
from datetime import datetime
from django.conf import settings
from django.db import models
from discounts.models import Coupon


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    coupon = models.ForeignKey(Coupon, related_name="coupon", on_delete=models.SET_NULL, blank=True, null=True)
    ordered_date = models.DateTimeField()
    paid = models.BooleanField(default=False)
    billing_address = models.CharField(max_length=13, blank=True, null=True)

    def __str__(self):
        return f"{self.user} سفارشات"

    def total_price(self):
        total = 0
        order_book_lst = super().get_queryset().exclude(task=None)
        for order_book in order_book_lst:
            total += order_book.each_price
        return total

    def check_coupon_validation(self):
        now = datetime.now()
        if self.coupon.expiration_date > now and self.coupon.extension_date <= now:
            coupon_validation = True
        else:
            coupon_validation = False
        return coupon_validation

    def price_with_coupon_discount(self):
        final_price = self.total_price
        if self.coupon is not None:
            if self.check_coupon_validation is True:
                if self.coupon.flat_amount in None:
                    final_price = self.total_price - self.coupon.cash - (1-self.coupon.percentage)

                else:
                    if self.coupon.flat_amount * self.coupon.percentage >= self.total_price:
                        final_price = self.total_price - self.coupon.flat_amount
                    else:
                        final_price = self.total_price * (1 - self.coupon.percentage)

        return final_price


class OrderBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    Order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"سفارش {self.id} - {self.book.title}"

    def each_price(self):
        price = self.book.get_final_price * self.quantity
        return price
