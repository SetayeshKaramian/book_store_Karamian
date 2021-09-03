from book.models import Book
from datetime import datetime
from django.conf import settings
from django.db import models
from discounts.models import Coupon
from django.shortcuts import reverse
from users.models import Address


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="کاربر")
    coupon = models.ForeignKey(Coupon, related_name="coupon", on_delete=models.SET_NULL,
                               blank=True, null=True, verbose_name="کپن")
    ordered_date = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False, verbose_name="پرداخت شده")
    billing_address = models.CharField(max_length=13, blank=True, null=True, verbose_name="شماره حساب")
    shipping_address = models.ForeignKey(Address, default=None, blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "سفارش"
        verbose_name_plural = "سفارشات"

    def __str__(self):
        return f"{self.user} سفارشات"

    def get_absolute_url(self):
        return reverse('cart', args=[str(self.id)])

    # sum of all orderbook prices without any discount
    def total_price(self):
        total = 0
        for order_book in self.book.all():
            total += order_book.each_price()
        return total

    # add discount to total_price
    def price_with_coupon_discount(self):
        final_price = self.total_price()
        if self.coupon is not None:
            if self.coupon.flat_fee is None:
                final_price = self.total_price() - self.coupon.cash - (1 - self.coupon.percentage)

            else:
                if self.coupon.flat_fee * self.coupon.percentage >= self.total_price():
                    final_price = self.total_price() - self.coupon.flat_fee
                else:
                    final_price = self.total_price() * (1 - self.coupon.percentage)

        """If the final_price after discount was less than zero, equal it to zero 
        so we don't owe money to customers for their shoppings :D"""
        if final_price < 0:
            final_price = 0

        return int(final_price)


class OrderBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='books', verbose_name="کتاب")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='book', verbose_name="سفارش")
    quantity = models.PositiveIntegerField(default=1, verbose_name="تعداد")

    class Meta:
        verbose_name = "اقلام سفارش"
        verbose_name_plural = "اقلام سفارش"

    def __str__(self):
        return f"{self.quantity} تا از {self.book}"

    # multiple quantity and book price
    def each_price(self):
        book_price = self.book.get_final_price()
        quantity = self.quantity
        total_price = book_price * quantity
        return total_price
