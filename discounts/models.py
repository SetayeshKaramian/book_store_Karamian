from django.db import models


# Create models.
class Coupon(models.Model):
    code = models.CharField(max_length=10, unique=True)
    percentage = models.FloatField(default=0, blank=True)
    flat_amount = models.IntegerField(default=None, blank=True, null=True)
    cash = models.IntegerField(default=0)
    expiration_date = models.DateTimeField()
    extension_date = models.DateTimeField()

    def __str__(self):
        return self.code


class Discount(models.Model):
    title = models.CharField(max_length=50)
    percentage = models.FloatField(default=0)
    flat_amount = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.title
