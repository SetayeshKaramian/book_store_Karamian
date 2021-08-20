from django.conf import settings
from django.db import models
from book.models import Book
from discounts.models import Coupon
from django.conf import settings


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    coupon = models.ForeignKey(Coupon, related_name="coupon", on_delete=models.SET_NULL, blank=True, null=True)
    ordered_date = models.DateTimeField()
    paid = models.BooleanField(default=False)
    billing_address = models.CharField(max_length=13, blank=True, null=True)

    def __str__(self):
        return f"{self.user} سفارشات"

    def total_price(self):
        pass


class OrderBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1)
    Order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f"سفارش {self.id} - {self.book.title}"
