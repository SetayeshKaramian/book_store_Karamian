from django.db import models
from django.shortcuts import reverse
from django_extensions.db.fields import AutoSlugField
from discounts.models import Discount


class Category(models.Model):
    title = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=100)
    category = models.ManyToManyField(Category, related_name='book')
    description = models.TextField()
    time_add = models.DateTimeField(auto_now_add=True)
    price = models.PositiveIntegerField(default=0)
    discount = models.ForeignKey(Discount, related_name="discount", on_delete=models.SET_NULL, blank=True, null=True)
    image = models.ImageField(upload_to='covers/', blank=True, null=True)
    storage = models.PositiveIntegerField(default=1)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

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
