from django.contrib import admin
from .models import Book, Category


class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ('admin_image_display', 'title', 'author', 'price', 'storage')
    list_filter = ('author', 'publisher', 'category__title')
    search_fields = ('title', 'publisher', 'author', 'category__title')
    ordering = ['time_add', 'title']

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    search_fields = ['title']

admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
