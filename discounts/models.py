from django.db import models


# Coupon will be add in the end of cart (ForeignKey to Order model)
class Coupon(models.Model):
    code = models.CharField(max_length=10, unique=True, verbose_name="کد")
    percentage = models.FloatField(default=0, blank=True, verbose_name="درصد")
    # flat_amount: max possible amount for discount
    max_amount = models.IntegerField(default=None, blank=True, null=True, verbose_name="حداکثر تحفیف")
    flat_fee = models.IntegerField(default=0, verbose_name="تخفیف ثابت")
    expiration_date = models.DateTimeField(verbose_name="انقضا")

    class Meta:
        verbose_name = "کپن"
        verbose_name_plural = "کپن‌ها"

    def __str__(self):
        return self.code


# Discount for each book (ForeignKey to Book model)
class Discount(models.Model):
    title = models.CharField(max_length=50, verbose_name="عنوان")
    # flat_amount: max possible amount for discount
    percentage = models.FloatField(default=0, verbose_name="درصد")
    flat_amount = models.PositiveIntegerField(blank=True, null=True, verbose_name="مبلغ ثابت")

    class Meta:
        verbose_name = "تخفیف"
        verbose_name_plural = "تخفیف‌ها"

    def __str__(self):
        return self.title
