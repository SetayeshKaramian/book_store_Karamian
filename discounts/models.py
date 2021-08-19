from django.db import models
from book.models import Book


# Create models.
class Coupon(models.Model):
    code = models.CharField(max_length=10, unique=True)
    percentage = models.FloatField(default=0, blank=True)
    flat_amount = models.IntegerField(default=None, blank=True, null=True)
    cash = models.IntegerField(default=0, blank=True)
    expiration_date = models.DateTimeField()
    extension_date = models.DateTimeField()

    def __str__(self):
        return self.code


class DiscountPercent(models.Model):
    books = models.ManyToManyField(Book, related_name="DPbooks")
    percentage = models.FloatField()


class DiscountUpTo(models.Model):
    books = models.ManyToManyField(Book, related_name="DUTbooks")
    percentage = models.FloatField()
    flat_amount = models.IntegerField()
