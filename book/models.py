from django.db import models
from django.shortcuts import reverse
from django.utils.safestring import mark_safe
from django_extensions.db.fields import AutoSlugField
from discounts.models import Discount


class Category(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name="عنوان")

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    author = models.CharField(max_length=200, verbose_name="نویسنده")
    publisher = models.CharField(max_length=100, verbose_name="ناشر")
    category = models.ManyToManyField(Category, related_name='book', verbose_name="دسته‌بندی")
    description = models.TextField(verbose_name="توضیحات")
    time_add = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")
    price = models.PositiveIntegerField(default=0, verbose_name="قیمت")
    discount = models.ForeignKey(Discount, related_name="discount", on_delete=models.SET_NULL, blank=True, null=True,
                                 verbose_name="تخفیف")
    image = models.ImageField(upload_to='covers/', default="covers/blank.jpg", blank=False, null=True,
                              verbose_name="عکس")
    storage = models.PositiveIntegerField(default=1, verbose_name="موجودی")
    slug = models.SlugField(unique=True, verbose_name="عنوان رسمی برای لینک")

    class Meta:
        verbose_name = "کتاب"
        verbose_name_plural = "کتاب‌ها"

    def __str__(self):
        return self.title

    # For admin site to be able to display book images.
    def admin_image_display(self):
        return mark_safe(f'<img src="{self.image.url}" width="{90}" height={125} />')

    admin_image_display.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])

    def get_final_price(self):
        if self.discount is None:
            final_price = self.price
        else:
            if self.discount.flat_amount is None:
                final_price = self.price * (1 - self.discount.percentage)
            else:
                if self.discount.flat_amount * self.discount.percentage >= self.price:
                    final_price = self.price - self.discount.flat_amount
                else:
                    final_price = self.price * (1 - self.discount.percentage)
        return int(final_price)
