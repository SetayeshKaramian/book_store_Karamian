from django.contrib import admin
from .models import Book, Category


class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ('admin_image_display', 'title', 'author', 'price', 'storage')
    list_filter = ('time_add', 'price', 'discount', 'storage', 'author', 'publisher', 'category')
    search_fields = ('title', 'publisher', 'author', 'category')
    ordering = ['time_add', 'title']


admin.site.register(Book, BookAdmin)
admin.site.register(Category)
