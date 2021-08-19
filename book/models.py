from django.db import models


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
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title