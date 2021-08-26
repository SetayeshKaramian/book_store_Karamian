from django.db import models


# Coupon will be add in the end of cart (ForeignKey to Order model)
class Coupon(models.Model):
    code = models.CharField(max_length=10, unique=True)
    percentage = models.FloatField(default=0, blank=True)
    # flat_amount: max possible amount for discount
    flat_amount = models.IntegerField(default=None, blank=True, null=True)
    cash = models.IntegerField(default=0)
    expiration_date = models.DateTimeField()
    extension_date = models.DateTimeField()

    class Meta:
        verbose_name = "کپن"
        verbose_name_plural = "کپن‌ها"

    def __str__(self):
        return self.code


# Discount for each book (ForeignKey to Book model)
class Discount(models.Model):
    title = models.CharField(max_length=50)
    # flat_amount: max possible amount for discount
    percentage = models.FloatField(default=0)
    flat_amount = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        verbose_name = "تخفیف"
        verbose_name_plural = "تخفیف‌هاها"

    def __str__(self):
        return self.title
